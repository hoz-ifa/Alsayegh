[app]

# (str) Title of your application
title = Alsayegh Pro

# (str) Package name
package.name = alsayeghpro

# (str) Package domain (needed for android packaging)
package.domain = org.hozifa

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
# الأهم: قمنا بتقليل المتطلبات لضمان نجاح البناء
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android NDK directory (if empty, it will be automatically downloaded)
android.ndk_path = 

# (str) Android SDK directory (if empty, it will be automatically downloaded)
android.sdk_path = 

# (list) Architecture to build for (arm64-v8a is best for your Honor phone)
android.archs = arm64-v8a

# (bool) use buildozer/p4a managed android.entrypoint
android.entrypoint = main.py

# (str) python-for-android branch to use
p4a.branch = master

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = arm64-v8a

# (bool) allow backup
android.allow_backup = True

# (str) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1

[buildozer]

# (int) log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1
