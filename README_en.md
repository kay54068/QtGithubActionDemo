
| [chinese][chinese-link] | [english][english-link] |
|-------------------------|-------------------------|


Qt Github Actions Demo
=======

# Introduction


This repository is the demo example of Qt Framework App on Github Actions

> Only support QMake, cmake has not been implemented

## Project information


| [License][license-link] | [Release][release-link] | [Download][download-link] | [Issues][issues-link] | [Wiki][wiki-links] |
|-------------------------|-------------------------|---------------------------|-----------------------|--------------------|
| ![license-badge]        | ![release-badge]        | ![download-badge]         | ![issues-badge]       | ![wiki-badge]      |

[win-link]: https://github.com/kay54068/QtGithubActionDemo/actions?query=workflow%3AWindows-MinGW "WindowsAction"
[win-mingw-badge]: https://github.com/kay54068/QtGithubActionDemo/workflows/Windows-MinGW/badge.svg  "Windows MSVC"

[win-link]: https://github.com/kay54068/QtGithubActionDemo/actions?query=workflow%3AWindows-MSVC "WindowsAction"
[win-msvc-badge]: https://github.com/kay54068/QtGithubActionDemo/workflows/Windows-MSVC/badge.svg  "Windows MSVC"

[linux-link]: https://github.com/kay54068/QtGithubActionDemo/actions?query=workflow%3AUbuntu "UbuntuAction"
[linux-badge]: https://github.com/kay54068/QtGithubActionDemo/workflows/Linux/badge.svg "Ubuntu"

[macos-link]: https://github.com/kay54068/QtGithubActionDemo/actions?query=workflow%3AMacOS "MacOSAction"
[macos-badge]: https://github.com/kay54068/QtGithubActionDemo/workflows/MacOS/badge.svg "MacOS"

[android-link]: https://github.com/kay54068/QtGithubActionDemo/actions?query=workflow%3AAndroid "AndroidAction"
[android-badge]: https://github.com/kay54068/QtGithubActionDemo/workflows/Android/badge.svg "Android"

[ios-link]: https://github.com/kay54068/QtGithubActionDemo/actions?query=workflow%3AIOS "IOSAction"
[ios-badge]: https://github.com/kay54068/QtGithubActionDemo/workflows/IOS/badge.svg "IOS"

[release-link]: https://github.com/kay54068/QtGithubActionDemo/releases "Release status"
[release-badge]: https://img.shields.io/github/release/kay54068/QtGithubActionDemo.svg?style=flat-square "Release status"

[download-link]: https://github.com/kay54068/QtGithubActionDemo/releases/latest "Download status"
[download-badge]: https://img.shields.io/github/downloads/kay54068/QtGithubActionDemo/total.svg?style=flat-square "Download status"

[license-link]: https://github.com/kay54068/QtGithubActionDemo/blob/master/LICENSE "LICENSE"
[license-badge]: https://img.shields.io/badge/license-MIT-blue.svg "MIT"


[issues-link]: https://github.com/kay54068/QtGithubActionDemo/issues "Issues"
[issues-badge]: https://img.shields.io/badge/github-issues-red.svg?maxAge=60 "Issues"

[wiki-links]: https://github.com/kay54068/QtGithubActionDemo/wiki "wiki"
[wiki-badge]: https://img.shields.io/badge/github-wiki-181717.svg?maxAge=60 "wiki"


[english-link]: https://github.com/kay54068/QtGithubActionDemo/blob/master/README_EN.md "english README"

[chinese-link]: https://github.com/kay54068/QtGithubActionDemo/blob/master/README.md "中文 README"



# Support operation system

| [Windows][win-link]                   |
|---------------------------------------|
| ![win-mingw-badge]  ![win-msvc-badge] |



| [Linux][linux-link] |
|----------------------|
| ![linux-badge]      |

| [MacOS][macos-link] |
|---------------------|
| ![macos-badge]      |


| [Android][android-link] |
|-------------------------|
| ![android-badge]        |


| [IOS][ios-link] |
|-----------------|
| ![ios-badge]    |



# Support QT version

| Qt version |
|------------|
| 5.9.9      |
| 5.10.1     |
| 5.11.3     |
| 5.12.10    |
| 5.13.2     |
| 5.14.2     |
| 5.15.2     |
| 6.0.x      |


- Qt version with compiler description

| Qt version | MSVC     | Mingw   | Linux  | MacOS    | Android                          | IOS      |
|------------|----------|---------|--------|----------|----------------------------------|----------|
| 5.9.9      | msvc2015 | mingw53 | gcc_64 | clang_64 | armeabi-v7a/arm64-v8a/x86/x86_64 | clang_64 |
| 5.10.1     | msvc2015 | mingw53 | gcc_64 | clang_64 | armeabi-v7a/arm64-v8a/x86/x86_64 | clang_64 |
| 5.11.3     | msvc2015 | mingw73 | gcc_64 | clang_64 | armeabi-v7a/arm64-v8a/x86/x86_64 | clang_64 |
| 5.12.10    | msvc2017 | mingw73 | gcc_64 | clang_64 | armeabi-v7a/arm64-v8a/x86/x86_64 | clang_64 |
| 5.13.2     | msvc2017 | mingw73 | gcc_64 | clang_64 | armeabi-v7a/arm64-v8a/x86/x86_64 | clang_64 |
| 5.14.2     | msvc2017 | mingw73 | gcc_64 | clang_64 | armeabi-v7a/arm64-v8a/x86/x86_64 | clang_64 |
| 5.15.2     | msvc2019 | mingw81 | gcc_64 | clang_64 | armeabi-v7a/arm64-v8a/x86/x86_64 | clang_64 |
| 6.0.x      | msvc2019 | mingw81 | gcc_64 | clang_64 | armeabi-v7a/arm64-v8a/x86/x86_64 | clang_64 |


# Github Action flow

1. checkout current commit
2. Configure the Python environment
3. Configure the system environment variables
4. Install the use of the kit
5. Download QT Compilation Environment 
6. Build
7. Package
8. Upload to GitHub Artifacts
9. Upload to GitHub Release Item (only contact with Git Tag )

# Way of use

## Qt part
- Step 1.  Qt  `yourprofile.pro` profie Added content:

   ```py
   CONFIG(debug,debug|release) {
      DESTDIR = $$absolute_path($${_PRO_FILE_PWD_}/bin/debug)
   } else {
      DESTDIR = $$absolute_path($${_PRO_FILE_PWD_}/bin/release)
   }

   ```
- Step 2. Move Source Code to `src` Directory (selective modification)
  
   e.g.
   ```py
   SOURCES += \
         src/main.cpp

   RESOURCES += src/qml.qrc  
   ```

## Github action Part
- Step 1. Move the following directory below your QT project
   - util/
   - .github/
- Step 2. modify util/ci/config.py
   ```py
   app_name = 'your app name'
   pro_name = 'your pro file name'
   ```
- Step 3. Modify * .yml Qt_Modules configuration before needed

   ref api path:
   https://download.qt.io/online/qtsdkrepository/



# Notice
1. The preset setting GitHub ActionS startup condition is push / pull request, if the following file is modified to trigger the automation process：
   ```
      - '*.pro'
      - 'src/**'
      - '.github/workflows/build_android.yml'
    ```
    📃 Please modify itself `.github/workflows/*.yml` , `on:` key configuration

2. If the push will trigger all platform Actions, automation deployment and generates release file, please download:

   [download-link]


# TODO
- [ ] Support cmake configuration
- [ ] IOS support `.ips` file output and packaged program 
- [ ] linux support [appimage](https://appimage.org/) package program 
- [ ] Windows support [Qt IFW](https://doc.qt.io/qtinstallerframework/ifw-overview.html) or [INNO](https://jrsoftware.org/isinfo.php) related setup packaging program


# Reference resource
- https://docs.github.com/en/actions
- https://github.com/kay54068/qtcreator-doxygen
- https://github.com/jaredtao/HelloActions-Qt
- https://download.qt.io/online/qtsdkrepository/