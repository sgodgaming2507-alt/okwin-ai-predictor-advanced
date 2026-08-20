[app]

# Application name
title = Advanced AI Analytics

# Package name
package.name = advancedanalytics

# Package domain
package.domain = org.example

# Source directory
source.dir = .

# Python file
source.main = main.py

# Application version
version = 1.0

# Required Python packages
requirements = python3,kivy

# Screen orientation
orientation = portrait

# Android settings
fullscreen = 0

# Android API
android.api = 35
android.minapi = 23

# Android architecture
android.archs = arm64-v8a

# Android permissions
android.permissions = INTERNET

# Keep build output
android.release_artifact = %(name)s-%(version)s-release.apk
android.debug_artifact = %(name)s-%(version)s-debug.apk

# Android backup
android.allow_backup = True

# Log level
log_level = 2


[buildozer]

# Build directory
build_dir = .buildozer

# Output directory
bin_dir = bin

# Verbose logging
log_level = 2

# Warning timeout
warn_on_root = 0
