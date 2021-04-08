import common as c
from config import app_name, os_name, os_arch, pro_file 
import os
import shutil
import multiprocessing

c.print('>> Building {} on {} arch {}'.format(app_name, os_name, os_arch))

env_script = 'true'
qmake_cmd = 'qmake CONFIG+=release "{}"'.format(pro_file)

qt_dir_prefix = os.path.abspath('qt')


os.environ['PKG_CONFIG_PATH'] = qt_dir_prefix + '/lib/pkgconfig'
os.environ['Qt5_Dir'] = qt_dir_prefix
os.environ['Qt5_DIR'] = qt_dir_prefix
os.environ['QT_PLUGIN_PATH'] = qt_dir_prefix + '/plugins'
os.environ['QML2_IMPORT_PATH'] = qt_dir_prefix + '/qml'

if os_name == 'linux':
    os.environ['LD_LIBRARY_PATH'] = os.environ['LD_LIBRARY_PATH'] + ':' + qt_dir_prefix + '/lib'
    make_cmd = 'make -j{}'.format(multiprocessing.cpu_count())
elif os_name == 'macos':
    make_cmd = 'make -j{}'.format(multiprocessing.cpu_count())
elif os_name == 'ios':
    qmake_cmd = 'qmake -r -spec macx-ios-clang CONFIG+=release CONFIG+=iphoneos "{}"'.format(pro_file)
    make_cmd = 'make -j{}'.format(multiprocessing.cpu_count())
elif os_name == 'android':
    #https://doc.qt.io/qt-5/qmake-variable-reference.html#android-abi
    qmake_cmd = 'qmake CONFIG+=release "{}{}" {}'.format('ANDROID_ABIS=', os_arch, pro_file)
    make_cmd = 'make -j{} {}'.format(multiprocessing.cpu_count(), 'apk' )
else: ## mingw or msvc
    
    if os_arch == 'mingw':
        qmake_cmd = 'qmake "{}"'.format(pro_file)
        make_cmd = 'mingw32-make'
    else: # msvc
        make_cmd = 'nmake'
        msvc_version = os.getenv('msvc_version', '2019/Enterprise')    
        env_script = 'C:/Program Files (x86)/Microsoft Visual Studio/{}/VC/Auxiliary/Build/'.format(msvc_version)
        
        if os_name == 'win32_msvc':
            env_script += 'vcvars32.bat'
        elif os_name == 'win64_msvc':
            env_script += 'vcvars64.bat'


if os_arch == 'mingw':
    os.environ['PATH'] = os.path.abspath('qt/bin') + ';' + os.path.abspath('mingwTools/bin') + ';' + os.environ['PATH']
elif os_arch == 'msvc':
    os.environ['PATH'] = os.path.abspath('qt/bin') + ';' + os.environ['PATH']
else:
    os.environ['PATH'] = os.path.abspath('qt/bin') + ':' + os.environ['PATH']


build_dir = 'build'
shutil.rmtree(build_dir, ignore_errors=True)
os.mkdir(build_dir)

env_cmd = '"{}"'.format(env_script)


os.chdir(build_dir)
c.run('{} && {} && {}'.format(env_cmd, qmake_cmd, make_cmd))
os.chdir('..')
