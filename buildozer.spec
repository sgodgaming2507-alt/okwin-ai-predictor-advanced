[app]

# (str) Title of your application
title = OKWin AI Predictor

# (str) Package name
package.name = okwinpredictor

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy==2.3.0,requests,urllib3,charset_normalizer,idna,certifi,openssl

# (str) python-for-android branch to use
p4a.branch = master

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

# (int) Target Android API
android.api = 33
android.build_tools_version = 33.0.2

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (int) Android NDK version to use
android.ndk = 25b

# (bool) Android logcat filters to use
android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

# (str) The Android arch to build for
android.archs = arm64-v8a

# (bool) enables Android auto backup feature
android.allow_backup = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
