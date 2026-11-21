<div align="center">
  <img src="https://raw.githubusercontent.com/netbox-community/netbox/main/docs/netbox_logo_light.svg" width="400" alt="نشان NetBox" />
  <p><strong>زیرساخت اصلی شبکه‌های خودکار</strong></p>
  <a href="https://github.com/netbox-community/netbox/releases"><img src="https://img.shields.io/github/v/release/netbox-community/netbox" alt="آخرین انتشار" /></a>
  <a href="https://github.com/netbox-community/netbox/blob/main/LICENSE.txt"><img src="https://img.shields.io/badge/license-Apache_2.0-blue.svg" alt="مجوز" /></a>
  <a href="https://github.com/netbox-community/netbox/graphs/contributors"><img src="https://img.shields.io/github/contributors/netbox-community/netbox?color=blue" alt="مشارکت‌کنندگان" /></a>
  <a href="https://github.com/netbox-community/netbox/stargazers"><img src="https://img.shields.io/github/stars/netbox-community/netbox?style=flat" alt="ستاره‌های گیت‌هاب" /></a>
  <a href="https://explore.transifex.com/netbox-community/netbox/"><img src="https://img.shields.io/badge/languages-17-blue" alt="زبان‌های پشتیبانی‌شده" /></a>
  <a href="https://github.com/netbox-community/netbox/actions/workflows/ci.yml"><img src="https://github.com/netbox-community/netbox/actions/workflows/ci.yml/badge.svg" alt="وضعیت یکپارچه‌سازی پیوسته" /></a>
  <p>
    <strong><a href="https://netboxlabs.com/community/">انجمن NetBox</a></strong> |
    <strong><a href="https://netboxlabs.com/netbox-cloud/">NetBox Cloud</a></strong> |
    <strong><a href="https://netboxlabs.com/netbox-enterprise/">NetBox Enterprise</a></strong>
  </p>
</div>

NetBox برای کمک به مهندسان شبکه ساخته شده است. بیش از یک دهه است که هزاران سازمان در سراسر جهان برای مدل‌سازی و مستندسازی زیرساخت شبکه از آن استفاده می‌کنند. NetBox مدل داده‌ای یکپارچه، گسترده و قابل‌دسترس برای منابع شبکه ارائه می‌دهد. رابط کاربری و APIهای آن همه‌چیز، از نقشهٔ کابل‌کشی تا پیکربندی تجهیزات، را پوشش می‌دهند و NetBox را به مرجع مرکزی داده‌های شبکه تبدیل می‌کنند. NetBox همچنین بخش اصلی پلتفرم [NetBox Labs](https://netboxlabs.com/) است که قابلیت‌های [کشف شبکه](https://netboxlabs.com/products/netbox-discovery/)، [اطمینان از عملکرد شبکه](https://netboxlabs.com/products/netbox-assurance/) و [مشاهده‌پذیری](https://netboxlabs.com/products/netbox-observability/) را هم ارائه می‌دهد.

<p align="center">
  <a href="#netboxs-role">نقش NetBox</a> |
  <a href="#why-netbox">چرا NetBox؟</a> |
  <a href="#getting-started">شروع کار</a> |
  <a href="#plugins">افزونه‌ها</a> |
  <a href="#get-involved">مشارکت</a> |
  <a href="#screenshots">تصاویر محیط برنامه</a>
</p>

<p align="center">
  <img src="docs/media/screenshots/home-light.png" width="600" alt="تصویر رابط کاربری NetBox" />
</p>

<a name="netboxs-role"></a>

## نقش NetBox

NetBox **مرجع اصلی داده‌ها** برای زیرساخت شبکه است. وظیفه‌اش تعریف و اعتبارسنجی _وضعیت مطلوب_ اجزا و منابع شبکه است. NetBox مستقیماً با گره‌های شبکه ارتباط برقرار نمی‌کند و داده‌ها را از طریق API در اختیار ابزارهای خودکارسازی، پایش و ارزیابی شبکه می‌گذارد. این تقسیم وظایف امکان ساخت سامانه‌ای پایدار و انعطاف‌پذیر را فراهم می‌کند.

<p align="center">
  <img src="docs/media/misc/reference_architecture.png" alt="معماری مرجع خودکارسازی شبکه" />
</p>

نمودار بالا معماری پیشنهادی استقرار شبکهٔ خودکار را نشان می‌دهد که در آن NetBox مرجع مرکزی وضعیت شبکه است. تیم شما می‌تواند ابزارهای مستقل را بر اساس نیاز جایگزین کند و روند کاری ماژولار و قابل پیش‌بینی داشته باشد.

<a name="why-netbox"></a>

## چرا NetBox؟

### مدل جامع داده

مدل یکپارچهٔ NetBox برای رک‌ها، تجهیزات، کابل‌ها، آدرس‌های IP، VLANها، مدارهای ارتباطی، برق، سرمایش، VPNها و دیگر منابع شبکه طراحی شده است. ارتباط میان این اشیا مدل‌سازی ساختارمند شبکه را ممکن می‌کند. مدل داده و پایگاه داده پس از نصب آمادهٔ استفاده‌اند.

### تمرکز توسعه

هدف NetBox فراهم کردن دسترسی برنامه‌پذیر به داده‌های زیرساخت شبکه است. توسعهٔ آن بر مدل‌سازی زیرساخت متمرکز است و APIهای آن امکان اتصال به ابزارهای تخصصی دیگر را فراهم می‌کنند.

### گسترش‌پذیری و سفارشی‌سازی

هر شبکه نیازهای خاص خودش را دارد. می‌توانید مدل دادهٔ NetBox را با فیلدها و برچسب‌های سفارشی گسترش دهید یا برای افزودن انواع جدید اشیا و قابلیت‌ها، افزونه بنویسید.

### مجوزهای انعطاف‌پذیر

مدیران می‌توانند مجوزهای کاربران و گروه‌ها را با جزئیات تعریف کنند. برای نمونه، می‌توان به گروهی فقط اجازهٔ مدیریت کابل‌ها را داد یا دسترسی هر تیم را به داده‌های یک مستأجر مشخص محدود کرد.

### اعتبارسنجی و قواعد حفاظتی سفارشی

در کنار قواعد داخلی، مدیران می‌توانند قواعد اعتبارسنجی سفارشی تعریف کنند تا اشیای تازه یا ویرایش‌شده با قواعد سازمان سازگار باشند یا حذف اشیای خاص، مانند تجهیزی با وضعیت `active`، ممنوع شود.

### تولید پیکربندی تجهیزات

NetBox می‌تواند با استفاده از الگوهای Jinja2 و داده‌های خودش، پیکربندی تجهیزات را تولید کند. الگوها را می‌توانید جداگانه بارگذاری کنید یا از منبعی بیرونی مانند مخزن Git دریافت کنید. پیکربندی تولیدشده از طریق REST API در دسترس است و با ابزارهایی مانند Ansible یا Salt می‌توان آن را روی تجهیزات اعمال کرد.

### اسکریپت‌های سفارشی

برای ساده‌سازی فرایندهایی مانند راه‌اندازی شعبهٔ جدید، می‌توانید اسکریپت سفارشی بنویسید، آن را بارگذاری کنید و از طریق رابط کاربری اجرا کنید. اسکریپت‌ها ورودی را از کاربر می‌گیرند و مراحل لازم را خودکار انجام می‌دهند.

### خودکارسازی رویدادها

قواعد رویداد می‌توانند در پاسخ به رویدادهای NetBox اسکریپت سفارشی یا وب‌هوک خروجی را اجرا کنند. برای نمونه، با افزودن تجهیز جدید، سامانهٔ پایش به‌روزرسانی می‌شود یا هنگام تخصیص بازهٔ IP، سرور DHCP به‌روزرسانی می‌شود.

### ثبت جامع تغییرات

NetBox ایجاد، ویرایش و حذف همهٔ اشیای تحت مدیریت را ثبت می‌کند. تغییرات به کاربر انجام‌دهنده نسبت داده می‌شوند و تغییرات مرتبط بر اساس شناسهٔ درخواست گروه‌بندی می‌شوند.

> [!NOTE]
> فهرست کامل قابلیت‌ها در [معرفی رسمی NetBox](https://netboxlabs.com/docs/netbox/introduction/) آمده است.

<a name="getting-started"></a>

## شروع کار

* برای آشنایی با محیط برنامه، [دموی عمومی](https://demo.netbox.dev/) را ببینید.
* برای استفاده از نسخهٔ میزبانی‌شده، [طرح رایگان NetBox Cloud](https://signup.netboxlabs.com/) را امتحان کنید.
* برای نصب روی زیرساخت خودتان، [راهنمای نصب فارسی](docs/installation/fa.md) را بخوانید. [راهنمای رسمی نصب](https://netboxlabs.com/docs/netbox/installation/) هم در دسترس است.
* برای استقرار کانتینری، از [تصویر Docker جامعهٔ کاربران](https://github.com/netbox-community/netbox-docker) استفاده کنید.
* [مستندات رسمی](https://netboxlabs.com/docs/netbox/) جزئیات بیشتری دربارهٔ NetBox ارائه می‌کنند.

<a name="plugins"></a>

## افزونه‌ها

افزونه‌ها با افزودن مدل‌ها، نماها و اتصال به سامانه‌های دیگر، قابلیت‌های NetBox را گسترش می‌دهند. چند نمونه در ادامه آمده است.

* [NetBox Branching](https://netboxlabs.com/docs/branching/) — کار با شاخه‌های مستقل و قابل‌ادغام داده‌های NetBox
* [NetBox Change Management](https://netboxlabs.com/docs/changes/) — اعمال قواعد بازبینی و تأیید روی تغییرات پیشنهادی شاخه‌ها (Cloud و Enterprise)
* [NetBox Custom Objects](https://netboxlabs.com/docs/custom-objects/) — تعریف انواع جدید اشیا برای گسترش ساختار دادهٔ NetBox
* [NetBox Asset Lifecycle](https://netboxlabs.com/docs/asset-lifecycle/) — پیگیری خرید تجهیزات از فهرست مواد تا سفارش خرید و ارسال (Cloud و Enterprise)
* [NetBox NDX](https://netboxlabs.com/docs/ndx/) — ورود خودکار تجهیزات، ماژول‌ها و سایر داده‌ها از [NetBox Data Exchange](https://netboxlabs.com/ndx/) (Cloud و Enterprise)
* [NetBox DNS](https://github.com/sys4/netbox-plugin-dns) — مدیریت ناحیه‌ها و رکوردهای DNS به‌عنوان مرجع معتبر
* [NetBox BGP](https://github.com/netbox-community/netbox-bgp) — مستندسازی و مدیریت نشست‌های BGP و سیاست‌های مسیریابی
* [NetBox WDM](https://github.com/jsenecal/netbox-wdm) — مدیریت طول‌موج‌های WDM، طرح‌های کانال ITU و سرویس‌های طول‌موج
* [NetBox Security](https://github.com/andy-shady-org/netbox-security/) — مدل‌سازی دیوارهٔ آتش، سیاست‌های امنیتی و NAT
* [همهٔ افزونه‌ها](https://netboxlabs.com/plugins/) — مشاهدهٔ فهرست کامل افزونه‌های موجود

<a name="get-involved"></a>

## مشارکت

* [@NetBoxOfficial](https://x.com/NetBoxOfficial) را در X دنبال کنید.
* در [انجمن گفتگو](https://github.com/netbox-community/netbox/discussions) و [Slack](https://netdev.chat/) به بحث‌ها بپیوندید.
* می‌توانید در گیت‌هاب [قابلیتی پیشنهاد دهید](https://github.com/netbox-community/netbox/issues/new?assignees=&labels=type%3A+feature&template=feature_request.yaml) یا [اشکالی گزارش کنید](https://github.com/netbox-community/netbox/issues/new?assignees=&labels=type%3A+bug&template=bug_report.yaml).
* پروژه از مشارکت جامعه استقبال می‌کند. برای شروع، [خلاصهٔ فارسی راهنمای مشارکت](docs/contributing-fa.md) و [راهنمای کامل مشارکت](CONTRIBUTING.md) را ببینید.

<a name="screenshots"></a>

## تصاویر محیط برنامه

<p align="center">
  <strong>داشبورد NetBox (حالت روشن)</strong><br />
  <img src="docs/media/screenshots/home-light.png" width="600" alt="داشبورد NetBox (حالت روشن)" />
</p>
<p align="center">
  <strong>داشبورد NetBox (حالت تیره)</strong><br />
  <img src="docs/media/screenshots/home-dark.png" width="600" alt="داشبورد NetBox (حالت تیره)" />
</p>
<p align="center">
  <strong>فهرست پیشوندها</strong><br />
  <img src="docs/media/screenshots/prefixes-list.png" width="600" alt="فهرست پیشوندها" />
</p>
<p align="center">
  <strong>نمای رک</strong><br />
  <img src="docs/media/screenshots/rack.png" width="600" alt="نمای رک" />
</p>
<p align="center">
  <strong>ردیابی کابل</strong><br />
  <img src="docs/media/screenshots/cable-trace.png" width="600" alt="ردیابی کابل" />
</p>
