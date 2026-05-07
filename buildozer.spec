[app]

# (str) الاسم الرسمي للتطبيق
title = Alsayegh Pro

# (str) اسم الحزمة العالمي (بدون مسافات)
package.name = alsayegh_pro_official

# (str) النطاق البرمجي
package.domain = com.hozifa.mining

# (str) مكان الكود المصدري (النقطة تعني المجلد الحالي)
source.dir = .

# (list) الملفات المدعومة (الصور، الخطوط، الأصوات)
source.include_exts = py,png,jpg,kv,atlas,ttf,wav,mp3,json

# (list) المكتبات الاحترافية المطلوبة
requirements = python3,kivy,requests,certifi,urllib3

# (str) نسخة التطبيق
version = 1.0.0

# (list) صلاحيات أندرويد الأساسية
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, VIBRATE

# (int) مستوى الـ API المستهدف (33 هو المعيار العالمي حالياً)
android.api = 33
android.minapi = 21
android.ndk = 25b

# (str) اتجاه الشاشة
orientation = portrait

# (bool) منع انطفاء الشاشة أثناء العمل
android.wakelock = True

# (list) المعماريات المدعومة ليعمل على كافة الهواتف
android.archs = arm64-v8a, armeabi-v7a

# (str) وضعية لوحة المفاتيح لمنع تداخل العناصر
android.window_softinput_mode = pan

# (bool) قبول رخصة الـ SDK تلقائياً
android.accept_sdk_license = True

[buildozer]
# (int) مستوى التنبيهات (2 يعطي تقارير واضحة)
log_level = 2

# (str) مسار إخراج ملف الـ APK النهائي
bin_dir = ./bin
