interface PluginConfig {
  [plugin: string]: object;
}

export function getPlugins(element: HTMLSelectElement): object {
  const plugins: PluginConfig = {};
  const labels = document.documentElement.dataset;

  // Enable "clear all" button for non-required fields
  if (!element.required) {
    plugins.clear_button = {
      title: labels.selectClear ?? 'Clear All',
      html: (data: Dict) =>
        `<i class="mdi mdi-close-circle ${data.className}" title="${data.title}"></i>`,
    };
  }

  // Enable individual "remove" buttons for items on multi-select fields
  if (element.hasAttribute('multiple')) {
    plugins.remove_button = {
      title: labels.selectRemove ?? 'Remove',
    };
  }

  // Enable drag-and-drop reordering of items on multi-select fields
  if (element.hasAttribute('multiple')) {
    plugins.drag_drop = {};
  }

  return {
    plugins: plugins,
  };
}
