import common as c
from config import qt_modules, qt_version, qt_dir, os_name
import sys
import xml.etree.ElementTree as ET

qt_modules_list = list(qt_modules.split())

c.print('>> Downloading Qt {} ({}) for {}'.format(qt_version, qt_modules_list, os_name))

# 5.9.9 : mingw53
# 5.10.1 : mingw53
# 5.11.3 : mingw73
# 5.12.10 : mingw73
# 5.13.2 : mingw73
# 5.14.2 : mingw73
# 5.15.2 : mingw81
# 6.0.0 : mingw81
WIN_MINGW_ARCH = {
            '5.9.9' : 53,
            '5.10.1' : 53,
            '5.11.3' : 73,
            '5.12.10' : 73,
            '5.13.2' : 73,
            '5.14.2' : 73,
            '5.15.2' : 81,
            '6.0.0' : 81
        }
# 5.9.9 :   msvc2015
# 5.10.1 :  msvc2015
# 5.11.3 :  msvc2015
# 5.12.10 : msvc2017
# 5.13.2 :  msvc2017
# 5.14.2 :  msvc2017
# 5.15.2 :  msvc2019
# 6.0.0 :   msvc2019
WIN_MSVC_ARCH = {
            '5.9.9' : '2015',
            '5.10.1' : '2015',
            '5.11.3' : '2015',
            '5.12.10' : '2017',
            '5.13.2' : '2017',
            '5.14.2' : '2017',
            '5.15.2' : '2019',
            '6.0.0' : '2019'
        }

def get_windows_arch(arch, os_bit, qtver):
    os_bit_str={
        32 : 'win32',
        64 : 'win64'
    }
    
    if arch == 'mingw':
        arch_ver= WIN_MINGW_ARCH
    else: # msvc
        arch_ver= WIN_MSVC_ARCH
        
    result_str = '{}_{}{}'.format(os_bit_str.get(os_bit,"") , arch , arch_ver.get(qtver,""))
    c.print('>>> windows arch: {}'.format(result_str))
    return result_str

def get_windows_qt_dir_prefix(arch, os_bit, qtver):

    if arch == 'mingw':
        arch_ver= WIN_MINGW_ARCH
    else: # msvc
        arch_ver= WIN_MSVC_ARCH
    
    if arch == 'msvc' and os_bit == 32:
        m_str = '{}{}'.format(arch, arch_ver.get(qtver,""))
    else:
        m_str = '{}{}_{}'.format(arch, arch_ver.get(qtver,""), os_bit)
        
    result_str = '{}/{}'.format(qtver, m_str)
    c.print('>>> qt_dir_prefix: {}'.format(result_str))
    return result_str


def get_windows_mingw_tool_prefix( os_bit, qtver):
    
    arch_ver= WIN_MINGW_ARCH
    result_str = '{}{}0_{}'.format('mingw', arch_ver.get(qtver,""), os_bit)
    c.print('>>> mingw_tool_prefix: {}'.format(result_str))
    return result_str

def download_mingw_tool():
    qt_version_dotless = qt_version.replace('.', '')
    base_url = 'https://download.qt.io/online/qtsdkrepository/windows_x86/desktop/tools_mingw/'
    updates_file = 'Updates-{}-{}-{}.xml'.format(qt_version, os_name, 'qttool')
    c.download(base_url + '/Updates.xml', updates_file)

    updates = ET.parse(updates_file)
    updates_root = updates.getroot()
    all_modules = {}
    for i in updates_root.iter('PackageUpdate'):
        name = i.find('Name').text
        
        if 'debug' in name or not kit_arch in name:
            continue

        archives = i.find('DownloadableArchives')
        if archives.text is None:
            continue
        c.print(' archives: {}'.format(archives))
        archives_parts = archives.text.split(',')
        version = i.find('Version').text
        c.print(' version: {}'.format(version))
        for archive in archives_parts:
            archive = archive.strip()
            parts = archive.split('-')
            module_name = parts[0]
            all_modules[module_name] = {'package': name, 'file': version + archive}
    if len(sys.argv) > 1:  # handle subcommand
        if sys.argv[1] == 'list':
            c.print('Available modules:')
            for k in iter(sorted(all_modules.keys())):
                c.print(k, '---', all_modules[k]['file'])
        exit(0)
        
    file_name = all_modules[module_name]['file']
    package = all_modules[module_name]['package']
    c.print('download url: {}'.format(base_url + '/' + package + '/' + file_name))
    c.download(base_url + '/' + package + '/' + file_name, file_name)
    c.extract(file_name, '.')


def downloadQtPackge():
    qt_version_dotless = qt_version.replace('.', '')
    base_url = 'https://download.qt.io/online/qtsdkrepository/{}/{}/qt5_{}' \
        .format(os_url, target_platform ,qt_version_dotless)
    updates_file = 'Updates-{}-{}.xml'.format(qt_version, os_name)
    c.download(base_url + '/Updates.xml', updates_file)

    updates = ET.parse(updates_file)
    updates_root = updates.getroot()
    all_modules = {}
    for i in updates_root.iter('PackageUpdate'):
        name = i.find('Name').text
        if 'debug' in name or not kit_arch in name:
            continue

        archives = i.find('DownloadableArchives')
        if archives.text is None:
            continue

        archives_parts = archives.text.split(',')
        version = i.find('Version').text
        for archive in archives_parts:
            archive = archive.strip()
            parts = archive.split('-')
            module_name = parts[0]
            all_modules[module_name] = {'package': name, 'file': version + archive}

    if len(sys.argv) > 1:  # handle subcommand
        if sys.argv[1] == 'list':
            c.print('Available modules:')
            for k in iter(sorted(all_modules.keys())):
                c.print(k, '---', all_modules[k]['file'])
        exit(0)


    for module in qt_modules_list:
        if module not in all_modules:
            c.print('>> Required module {} not available'.format(module))
            continue
        file_name = all_modules[module]['file']
        package = all_modules[module]['package']
        c.download(base_url + '/' + package + '/' + file_name, file_name)
        c.extract(file_name, '.')

## linux
if os_name == 'linux':
    os_url = 'linux_x64'
    kit_arch = 'gcc_64'
    qt_dir_prefix = '{}/gcc_64'.format(qt_version)
    target_platform = 'desktop'
## win32_msvc
elif os_name == 'win32_msvc':
    os_url = 'windows_x86'
    kit_arch =  get_windows_arch('msvc',32, qt_version)
    qt_dir_prefix = get_windows_qt_dir_prefix('msvc',32, qt_version)
    target_platform = 'desktop'
## win64_msvc
elif os_name == 'win64_msvc':
    os_url = 'windows_x86'
    kit_arch = get_windows_arch('msvc',64, qt_version)
    qt_dir_prefix = get_windows_qt_dir_prefix('msvc',64, qt_version)
    target_platform = 'desktop'
## win32_mingw
elif os_name == 'win32_mingw':
    os_url = 'windows_x86'
    kit_arch = get_windows_arch('mingw',32, qt_version)
    qt_dir_prefix = get_windows_qt_dir_prefix('mingw',32, qt_version)
    target_platform = 'desktop'
    
    download_mingw_tool()
    tool_var =  get_windows_mingw_tool_prefix(32,qt_version)
    tool_path = 'Tools/{}'.format(tool_var)
    c.print('>>> tool_path: {}'.format(tool_path))
    c.symlink(tool_path, 'mingwTools')
    # os.environ['PATH'] = os.path.abspath(tool_path) + ';' + os.environ['PATH']
    # c.print('>>> os.environ path: {}'.format(os.environ['PATH']))
    
## win64_mingw
elif os_name == 'win64_mingw':
    os_url = 'windows_x86'
    kit_arch = get_windows_arch('mingw',64, qt_version)
    qt_dir_prefix = get_windows_qt_dir_prefix('mingw',64, qt_version)
    target_platform = 'desktop'
    
    download_mingw_tool()
    tool_var =  get_windows_mingw_tool_prefix(64,qt_version)
    tool_path = 'Tools/{}/bin'.format(tool_var)
    c.print('>>> tool_path: {}'.format(tool_path))
    c.symlink(tool_path, 'mingwTools')
    # os.environ['PATH'] = os.path.abspath(tool_path) + ';' + os.environ['PATH']
    # c.print('>>> os.environ path: {}'.format(os.environ['PATH']))
## macos
elif os_name == 'macos':
    os_url = 'mac_x64'
    kit_arch = 'clang_64'
    qt_dir_prefix = '{}/clang_64'.format(qt_version)
    target_platform = 'desktop'
## ios
elif os_name == 'ios':
    os_url = 'mac_x64'
    kit_arch = 'ios'
    qt_dir_prefix = '{}/ios'.format(qt_version)
    target_platform = 'ios'
## android    
elif os_name == 'android':
    os_url = 'linux_x64'
    kit_arch = 'android'
    qt_dir_prefix = '{}/android'.format(qt_version)
    target_platform = 'android'


downloadQtPackge()

c.symlink(qt_dir_prefix, qt_dir)

c.print('>> Updating license')

config_name = qt_dir + '/mkspecs/qconfig.pri'
config = ''
with open(config_name, 'r') as f:
    config = f.read()

config = config.replace('Enterprise', 'OpenSource')
config = config.replace('licheck.exe', '')
config = config.replace('licheck64', '')
config = config.replace('licheck_mac', '')

with open(config_name, 'w') as f:
    f.write(config)
