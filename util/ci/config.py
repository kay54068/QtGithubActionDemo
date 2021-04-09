from os import getenv, path

app_name = 'QtGithubActionDemo'
pro_name = 'QtGithubActionDemo'

qt_version = getenv('qt_ver', '5.15.2')
## linux, macos, ios, android, win64_msvc, win32_msvc ,win64_mingw ,win32_mingw
os_name = getenv('qt_target', 'linux')
os_arch = getenv('qt_arch', 'gcc_64')

qt_modules = getenv('qt_modules', 'qtbase qtquickcontrols2 qtquickcontrols qtdeclarative icu qttools')
qt_dir = path.abspath('qt')

pro_file = path.abspath(path.dirname(__file__) + '/../../{}.pro'.format(pro_name))
#ts_files_dir = path.abspath(path.dirname(__file__) + '/../../translation')
