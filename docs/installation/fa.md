# راهنمای نصب NetBox Community

این راهنما نصب روی **Ubuntu 24.04** را از آرشیو انتشار یا Git تا راه‌اندازی سرویس HTTPS پوشش می‌دهد. در توزیع‌های دیگر، دستورهای نصب بسته‌ها ممکن است متفاوت باشند.

| وابستگی | نسخهٔ پشتیبانی‌شده |
| --- | --- |
| Python | 3.12، 3.13 یا 3.14 |
| PostgreSQL | 15 یا جدیدتر |
| Redis | 6.0 یا جدیدتر |

## ۱. PostgreSQL

اگر پایگاه دادهٔ PostgreSQL را از قبل آماده کرده‌اید، از همان استفاده کنید. در غیر این صورت، بستهٔ PostgreSQL را نصب و نسخهٔ آن را بررسی کنید.

```no-highlight
sudo apt update
sudo apt install -y postgresql
```

```no-highlight
psql -V
```

پوستهٔ PostgreSQL را با کاربر سیستمی `postgres` باز کنید.

```no-highlight
sudo -u postgres psql
```

دستورهای زیر پایگاه داده و نقش `netbox` را می‌سازند. مقدار `REPLACE_WITH_A_STRONG_PASSWORD` را با یک رمز تصادفی و قوی جایگزین کنید.

```postgresql
CREATE DATABASE netbox;
CREATE USER netbox WITH PASSWORD 'REPLACE_WITH_A_STRONG_PASSWORD';
ALTER DATABASE netbox OWNER TO netbox;
\connect netbox;
GRANT CREATE ON SCHEMA public TO netbox;
```

با دستور `\l` بررسی کنید کدگذاری پایگاه داده `UTF8` باشد و با `\q` از پوسته خارج شوید. سپس اتصال را آزمایش کنید. برای پایگاه دادهٔ راه دور، نام میزبان را جایگزین `localhost` کنید. پس از اتصال، `\conninfo` جزئیات اتصال را نشان می‌دهد.

```bash
psql --username netbox --password --host localhost netbox
```

## ۲. Redis

Redis حافظهٔ نهان و صف کارهای پس‌زمینهٔ NetBox را فراهم می‌کند. سرویس را نصب کنید، نسخه را بررسی کنید و مطمئن شوید دستور آخر `PONG` برمی‌گرداند.

```no-highlight
sudo apt install -y redis-server
```

```no-highlight
redis-server -v
```

```no-highlight
redis-cli ping
```

Redis را روی `localhost` یا شبکهٔ خصوصی نگه دارید. اگر از میزبان دیگری قابل دسترسی است، احراز هویت را فعال کنید. پردازشگرهای NetBox کارهای ذخیره‌شده در پایگاه `tasks` را اجرا می‌کنند، پس دسترسی نوشتن به آن را محدود کنید. [تنظیمات Redis](../configuration/required-parameters.md#redis)

## ۳. دریافت و پیکربندی NetBox

وابستگی‌های سیستمی را نصب کنید و نسخهٔ Python را بررسی کنید.

```no-highlight
sudo apt install -y python3 python3-pip python3-venv python3-dev \
build-essential libxml2-dev libxslt1-dev libffi-dev libpq-dev \
libssl-dev zlib1g-dev
```

```no-highlight
python3 -V
```

یکی از دو روش زیر را انتخاب کنید. در دستورها، `vX.Y.Z` را با تگ مدنظر از [انتشارهای پایدار NetBox](https://github.com/netbox-community/netbox/releases) جایگزین کنید.

### روش آرشیو انتشار

```no-highlight
sudo wget https://github.com/netbox-community/netbox/archive/refs/tags/vX.Y.Z.tar.gz
sudo tar -xzf vX.Y.Z.tar.gz -C /opt
sudo ln -s /opt/netbox-X.Y.Z/ /opt/netbox
```

### روش Git

```no-highlight
sudo mkdir -p /opt/netbox/
cd /opt/netbox/
```

```no-highlight
sudo apt install -y git
```

```no-highlight
sudo git clone https://github.com/netbox-community/netbox.git .
```

```
sudo git checkout vX.Y.Z
```

دستور Git بالا نسخهٔ رسمی را دریافت می‌کند. برای نصب کد سفارشی، نشانی مخزن را با نشانی فورک جایگزین کنید و شاخه یا تگی را انتخاب کنید که در همان فورک وجود دارد. برای محیط عملیاتی، نسخهٔ پایدار را مبنا قرار دهید.

### کاربر سرویس و فایل پیکربندی

برای اجرای سرویس‌ها، کاربر سیستمی `netbox` را بسازید و مالکیت پوشهٔ رسانه را به او بدهید. سپس از فایل نمونه یک کپی محلی بسازید.

```
sudo adduser --system --group netbox
sudo chown --recursive netbox /opt/netbox/netbox/media/
sudo chown --recursive netbox /opt/netbox/netbox/reports/
sudo chown --recursive netbox /opt/netbox/netbox/scripts/
```

```no-highlight
cd /opt/netbox/netbox/netbox/
sudo cp configuration_example.py configuration.py
```

فایل `configuration.py` را باز کنید و پنج تنظیم زیر را وارد کنید.

- `ALLOWED_HOSTS` شامل نام دامنه یا IPهایی است که کاربران با آن‌ها به NetBox وصل می‌شوند.
- `API_TOKEN_PEPPERS` شامل دست‌کم یک مقدار تصادفی برای توکن‌های API است. شناسهٔ عددی را از ۱ شروع کنید.
- `DATABASES` مشخصات اتصال PostgreSQL را نگه می‌دارد. نام پایگاه، نام کاربر، رمز، میزبان و پورت را مطابق مرحلهٔ اول تنظیم کنید.
- `REDIS` به دو پایگاه با شناسه‌های عددی جداگانه برای `tasks` و `caching` نیاز دارد. هر دو می‌توانند روی یک سرویس Redis باشند.
- `SECRET_KEY` یک کلید تصادفی و محرمانهٔ مختص همین استقرار است. طول پیشنهادی دست‌کم ۵۰ نویسه است. در استقرار چندسروری، مقدار آن باید روی همهٔ سرورها یکسان باشد.

برای تولید مقادیر تصادفی `SECRET_KEY` و `API_TOKEN_PEPPERS`، دستور زیر را جداگانه برای هر مقدار اجرا کنید. نمونه‌های کامل پیکربندی و وابستگی‌های اختیاری در [راهنمای نصب از آرشیو یا Git](3-netbox.md) آمده‌اند.

```no-highlight
python3 ../generate_secret_key.py
```

### نصب وابستگی‌ها و آماده‌سازی پایگاه داده

اگر محیط مجازی Python دیگری فعال است، ابتدا با `deactivate` از آن خارج شوید. سپس اسکریپت ارتقا را اجرا کنید. این اسکریپت محیط مجازی می‌سازد، وابستگی‌ها را نصب می‌کند، مهاجرت‌های پایگاه داده را اجرا می‌کند و مستندات محلی و فایل‌های ایستا را آماده می‌کند.

```no-highlight
sudo /opt/netbox/upgrade.sh
```

اگر نسخهٔ پیش‌فرض Python قدیمی‌تر است، مسیر یک نسخهٔ پشتیبانی‌شده را پس از `sudo` مشخص کنید.

```no-highlight
sudo PYTHON=/usr/bin/python3.12 /opt/netbox/upgrade.sh
```

### ایجاد حساب مدیر و آزمایش نصب

محیط مجازی را فعال کنید و با دستور زیر حساب مدیر بسازید. برای این حساب یک رمز قوی انتخاب کنید.

```no-highlight
source /opt/netbox/venv/bin/activate
```

```no-highlight
cd /opt/netbox/netbox
python3 manage.py createsuperuser
```

برای آزمایش نصب، سرور توسعه را موقتاً اجرا کنید. با نام یا IP تعریف‌شده در `ALLOWED_HOSTS` و پورت ۸۰۰۰ وارد شوید، سپس با حساب مدیر ورود را آزمایش کنید. پس از آزمایش، با `Ctrl+C` سرور را متوقف کنید. سرور توسعه را در محیط عملیاتی اجرا نکنید.

```no-highlight
python3 manage.py runserver 0.0.0.0:8000 --insecure
```

## ۴. Gunicorn و systemd

NetBox به‌عنوان برنامهٔ WSGI اجرا می‌شود. Gunicorn همراه NetBox نصب می‌شود. فایل پیکربندی آن را کپی کنید تا تغییرات محلی در ارتقاهای بعدی حفظ شوند. سپس فایل‌های سرویس را در systemd نصب و سرویس‌های وب و پردازشگر پس‌زمینه را فعال کنید.

```no-highlight
sudo cp /opt/netbox/contrib/gunicorn.py /opt/netbox/gunicorn.py
```

```no-highlight
sudo cp -v /opt/netbox/contrib/*.service /etc/systemd/system/
sudo systemctl daemon-reload
```

```no-highlight
sudo systemctl enable --now netbox netbox-rq
```

```no-highlight
systemctl status netbox.service
```

اگر نام کاربر یا گروه سرویس با `netbox` فرق دارد، فایل‌های سرویس را مطابق محیط خود ویرایش کنید. اگر سرویس اجرا نشد، لاگ را با `journalctl -eu netbox` بررسی کنید. برای سرور WSGI جایگزین، [راهنمای uWSGI](4b-uwsgi.md) را ببینید.

## ۵. سرور HTTP و HTTPS

برای محیط عملیاتی از گواهی معتبر، مثلاً [Let's Encrypt](https://letsencrypt.org/getting-started/)، استفاده کنید. گواهی و کلید را در مسیرهای مورد انتظار پیکربندی قرار دهید. کلید خصوصی را محرمانه نگه دارید. برای محیط آزمایشی، [نمونهٔ گواهی خودامضا](5-http-server.md#obtain-an-ssl-certificate) در دسترس است.

### nginx

nginx را نصب و پیکربندی نمونه را کپی کنید.

```no-highlight
sudo apt install -y nginx
```

```no-highlight
sudo cp /opt/netbox/contrib/nginx.conf /etc/nginx/sites-available/netbox
```

در فایل `/etc/nginx/sites-available/netbox`، مقدار `netbox.example.com` را با نام واقعی میزبان جایگزین کنید. این نام باید با `ALLOWED_HOSTS` هماهنگ باشد. مسیر گواهی و کلید را هم بررسی کنید. سپس سایت NetBox را فعال و nginx را راه‌اندازی مجدد کنید.

```no-highlight
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /etc/nginx/sites-available/netbox /etc/nginx/sites-enabled/netbox
```

```no-highlight
sudo systemctl restart nginx
```

### Apache

اگر Apache را انتخاب کرده‌اید، بسته را نصب و فایل نمونه را کپی کنید. پیش از فعال کردن سایت NetBox، مقادیر `ServerName` و مسیرهای گواهی و کلید را در فایل نمونه تنظیم کنید.

```no-highlight
sudo apt install -y apache2
```

```no-highlight
sudo cp /opt/netbox/contrib/apache.conf /etc/apache2/sites-available/netbox.conf
```

```no-highlight
sudo a2enmod ssl proxy proxy_http headers rewrite
sudo a2ensite netbox
sudo systemctl restart apache2
```

با HTTPS به نام یا IP سرور وصل شوید. اگر اتصال برقرار نشد، وضعیت سرویس وب، پورت و دیوارهٔ آتش را بررسی کنید. برای خطای ۵۰۲، وضعیت سرویس `netbox` و تطابق پورت مقصد پراکسی با پورت Gunicorn (به‌طور پیش‌فرض ۸۰۰۱) را بررسی کنید.

## مسیرهای دیگر و ارتقا

- [احراز هویت اختیاری LDAP](6-ldap.md)
- [نصب آزمایشی از بستهٔ Python در NetBox 4.7](3b-python-package.md) برای ارزیابی و ارائهٔ بازخورد در نظر گرفته شده است. روش آرشیو یا Git مسیر مرسوم نصب عملیاتی است.
- [خلاصهٔ فارسی روند ارتقا](upgrading-fa.md) و [راهنمای کامل ارتقا](upgrading.md)
- [نصب افزونه‌ها](../plugins/installation.md)
