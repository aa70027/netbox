#!/usr/bin/env python3
"""Install stable GitHub releases from the aa70027/netbox fork."""

import argparse
import fcntl
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

REPOSITORY = 'https://github.com/aa70027/netbox.git'
RELEASES = 'https://api.github.com/repos/aa70027/netbox/releases/latest'
SERVICES = ('netbox.service', 'netbox-rq.service')
VERSION = re.compile(r'(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)')


def installed_version(release_yaml):
    match = re.search(r'^version:\s*"([^"]+)"\s*$', release_yaml, re.MULTILINE)
    version = VERSION.fullmatch(match[1]) if match else None
    if version is None:
        raise ValueError('Expected a stable version in netbox/release.yaml.')
    return tuple(map(int, version.groups()))


def latest_release():
    request = Request(RELEASES, headers={
        'Accept': 'application/vnd.github+json',
        'User-Agent': 'netbox-fork-updater',
    })
    try:
        with urlopen(request, timeout=20) as response:
            data = json.load(response)
    except HTTPError as exc:
        if exc.code == 404:
            return None
        raise
    tag = data.get('tag_name', '')
    version = VERSION.fullmatch(tag.removeprefix('v'))
    if not tag.startswith('v') or not version or data.get('draft') or data.get('prerelease'):
        raise ValueError(f'Expected a published stable release, got {tag!r}.')
    return tag, tuple(map(int, version.groups()))


def update(root, state):
    def git(*args):
        return subprocess.check_output(('git', '-C', str(root), *args), text=True).strip()

    blocked = state / 'upgrade-in-progress'
    if blocked.exists():
        raise ValueError(f'Previous upgrade needs recovery. See {blocked}.')
    current = installed_version((root / 'netbox/release.yaml').read_text())
    remote = latest_release()
    if remote is None or remote[1] <= current:
        print('No newer stable release in the fork.')
        return
    tag, target_version = remote
    if Path(git('rev-parse', '--show-toplevel')).resolve() != root:
        raise ValueError('The installation path must be the root of a Git checkout.')
    if git('status', '--porcelain'):
        raise ValueError('Commit or move local changes before upgrading.')
    previous = git('rev-parse', 'HEAD')
    git('fetch', '--no-tags', REPOSITORY, f'refs/tags/{tag}')
    target = git('rev-parse', 'FETCH_HEAD^{commit}')
    git('merge-base', '--is-ancestor', previous, target)
    if installed_version(git('show', f'{target}:netbox/release.yaml')) != target_version:
        raise ValueError(f'{tag} does not match the version declared in the release.')
    blocked.write_text(f'Previous commit: {previous}\nTarget commit: {target}\nRelease: {tag}\n')
    subprocess.run(('systemctl', 'stop', *SERVICES), check=True)
    git('checkout', '--detach', target)
    subprocess.run(('bash', './upgrade.sh'), cwd=root, check=True)
    subprocess.run(('systemctl', 'start', *SERVICES), check=True)
    for service in SERVICES:
        subprocess.run(('systemctl', 'is-active', '--quiet', service), check=True)
    blocked.unlink()
    print(f'Installed {tag} from {REPOSITORY}.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path('/opt/netbox'))
    parser.add_argument('--state', type=Path, default=Path('/var/lib/netbox-fork-updater'))
    args = parser.parse_args()
    if os.geteuid() != 0:
        parser.error('Run as root to upgrade the installation and restart its services.')
    args.state.mkdir(mode=0o700, parents=True, exist_ok=True)
    try:
        with (args.state / 'lock').open('a') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            update(args.root.resolve(), args.state)
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f'NetBox upgrade stopped: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
