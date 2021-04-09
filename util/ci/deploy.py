import common as c
from config import os_name, app_name, pro_file, os_arch, qt_version
import os
import shutil
import multiprocessing

c.print('>> Deploy {} on {} arc {}'.format(app_name, os_name, os_arch))


qt_dir_prefix = os.path.abspath('qt')

os.environ['PKG_CONFIG_PATH'] = qt_dir_prefix + '/lib/pkgconfig'
os.environ['Qt5_Dir'] = qt_dir_prefix
os.environ['Qt5_DIR'] = qt_dir_prefix
os.environ['QT_PLUGIN_PATH'] = qt_dir_prefix + '/plugins'
os.environ['QML2_IMPORT_PATH'] = qt_dir_prefix + '/qml'


if os_name == 'linux':
    deploy_cmd = 'echo "Nothing"'
elif os_name == 'macos':
    deploy_cmd = 'macdeployqt bin/release/{}.app -qmldir=. -verbose=1 -dmg'.format(app_name)
elif os_name == 'ios':
    deploy_cmd = 'echo "Nothing"'
elif os_name == 'android':
    deploy_cmd = 'echo "Nothing"'
else:

    os.mkdir('bin/release/plugins')

    plugins = 'bin/release/plugins'
    app_file = 'bin/release/'+ app_name + '.exe'
    os.path.abspath('qt/bin')
    deploy_cmd = 'windeployqt --qmldir . --plugindir {} --no-translations --compiler-runtime {}'.format(plugins, app_file)


if os_arch == 'mingw':
    os.environ['PATH'] = os.path.abspath('qt/bin') + ';' + os.path.abspath('mingwTools/bin') + ';' + os.environ['PATH']
elif os_arch == 'msvc':
    os.environ['PATH'] = os.path.abspath('qt/bin') + ';' + os.environ['PATH']
else:
    os.environ['PATH'] = os.path.abspath('qt/bin') + ':' + os.environ['PATH']

c.run('{}'.format(deploy_cmd))


if os_arch == 'mingw' or os_arch == 'msvc':
    archive_name =  os.environ['archive_name']
    if archive_name:
        archive_file = '{}.{}'.format(archive_name, 'zip')
        c.print('>> archive {} from {}'.format(archive_file, os.path.abspath('bin/release/')))
        c.delete_extensions_file('bin/release/',('.qmlc','.ilk','.exp','.lib','.pdb','.qml'))
        c.make_zip('bin/release/', archive_file, mode='w')



