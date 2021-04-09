QtGithubActionsDemo
=======

# 介紹

此 Repository 為 Qt framework app 於 Github actions 的 Demo 範例

> 目前只支援 qmake , cmake 尚未實現

## 專案資訊


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


# 支援作業系統

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



# 支援Qt 版本

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


- Qt 版本搭配 compiler 說明

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

1. 切換至目前提交
2. 配置 python 環境
3. 配置所需的系統環境變數
4. 安裝相依的套件
5. 下載 Qt 編譯環境 
6. 建置
7. 打包
8. 上傳至 github artifacts
9. 上傳至 github Release 項目（ 只接受有加 git tag 之 commit）

# 使用方式

## Qt 部份
- Step 1.  Qt  `yourprofile.pro` profie 新增以下內容

   ```py
   CONFIG(debug,debug|release) {
      DESTDIR = $$absolute_path($${_PRO_FILE_PWD_}/bin/debug)
   } else {
      DESTDIR = $$absolute_path($${_PRO_FILE_PWD_}/bin/release)
   }

   ```
- Step 2.  移動source code 至 src 目錄 （選擇性修改)
  
   e.g.
   ```py
   SOURCES += \
         src/main.cpp

   RESOURCES += src/qml.qrc  
   ```

## Github action 部份
- Step 1. 將範例專案中以下目錄移至您的Qt 專案
   - util/
   - .github/
- Step 2. 修改 util/ci/config.py
   ```py
   app_name = 'your app name'
   pro_name = 'your pro file name'
   ```
- Step 3.依據需前修改 *.yml 的 qt_modules 配置

   ref api path:
   https://download.qt.io/online/qtsdkrepository/   



# 注意事項
1. 預設設定github actions 啟動條件為 push / pull_request 後, 若修改以下檔案才觸發自動化流程：
   ```
      - '*.pro'
      - 'src/**'
      - '.github/workflows/build_android.yml'
    ```
    📃 請自行修改 .github/workflows/xxx.yml 的 `on:` key 配置

2. 若psuh 一個 tag 將觸發所有平台的 actions , 自動執行自動化佈署並產生相關執行檔請至以下連結下載：

   [download-link]


# TODO
- [ ] 支援 cmake 配置
- [ ] IOS 支援 .ips 檔輸出及打包程序 
- [ ] linux 支援 [appimage](https://appimage.org/) 打包程序 
- [ ] Windows 支援 [Qt IFW](https://doc.qt.io/qtinstallerframework/ifw-overview.html) or [INNO](https://jrsoftware.org/isinfo.php) 相關 Setup 打包安裝檔程序


# 參考資源
- https://docs.github.com/en/actions
- https://github.com/kay54068/qtcreator-doxygen
- https://github.com/jaredtao/HelloActions-Qt
- https://download.qt.io/online/qtsdkrepository/