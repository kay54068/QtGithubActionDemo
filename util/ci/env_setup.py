import common as c
from config import app_name , os_name ,qt_version
import os
import shutil
import sys
import multiprocessing
archive_name = '{}_{}_Qt{}'.format(app_name, os_name, qt_version)

if len(sys.argv) > 1:  # handle subcommand
    if sys.argv[1] == 'appname':
        c.print(app_name)
    elif sys.argv[1] == 'archivename':
        c.print(archive_name)