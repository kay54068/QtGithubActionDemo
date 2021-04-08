from os import getenv, path

qt_version = getenv('qt_ver', '5.15.2')
os_name = getenv('qt_target', 'linux')
os_arch = getenv('qt_arch', 'gcc_64')
archive_name =  getenv('archive_name', '')
qt_modules = getenv('qt_modules', 'qtbase qtquickcontrols2 qtquickcontrols qtdeclarative icu qttools')
qt_dir = path.abspath('qt')
app_name = getenv('app_name', 'QtGithubActionDemo')
pro_file = path.abspath(path.dirname(__file__) + '/../../QtGithubActionDemo.pro')
#ts_files_dir = path.abspath(path.dirname(__file__) + '/../../translation')
