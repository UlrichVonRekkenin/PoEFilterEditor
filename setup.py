import sys

from cx_Freeze import Executable, setup

'''
To compile type "py -3 setup.py build_exe" in comand prompt
'''

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name='PoE Easy Filter Script Editor',
    version='1.0.3',
    description='',

    options={
        'build_exe': {
            'optimize': 2,
            'include_msvcr': True,
            'packages': ['os', 'sys', 'json'],
            'includes': ['re', 'PyQt4.QtCore', 'PyQt4.uic', 'PyQt4.Qt', 'PyQt4.QtGui'],
            'excludes': ['tkinter', 'QtSql', 'QtSvg', 'QtTest', 'QtWebKit', 'QtXml'],
            'include_files': ['filter_gui.ui', 'poe.ico'],
            'silent': True,
        }
    },

    executables=[
        Executable(
            targetName='PoE Easy Filter Script Editor.exe',
            script='main.pyw',
            excludes=['tkinter', 'QtSql', 'QtSvg', 'QtTest', 'QtWebKit', 'QtXml'],
            compress=True,
            icon='poe.ico',
            base=base
        )
    ]
)
