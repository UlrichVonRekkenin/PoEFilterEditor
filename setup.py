import sys
from cx_Freeze import setup, Executable

'''
To compile type "py -3 setup.py bdist_msi" in comand prompt
'''

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name='PoE Easy Filter Script Editor',
    version='1.0.2',
    description='',

    options={

        'build_exe': {
            'optimize': 1,
            'include_msvcr': True,
            'packages': ['os', 'sys', 'json'],
            'includes': ['re', 'PyQt4.QtCore', 'PyQt4.uic', 'PyQt4.Qt', 'PyQt4.QtGui'],
            'excludes': ['tkinter', 'QtSql', 'QtSvg', 'QtTest', 'QtWebKit', 'QtXml'],
            'include_files': ['config.json', 'filter_gui.ui', 'poe.png'],
            'silent': True,
            },

        'bdist_msi': {
            'data': {
                'Shortcut': [(
                    'DesktopShortcut',
                    'DesktopFolder',
                    'PoE Filter Lazy Editor', #  Name
                    'TARGETDIR',
                    '[TARGETDIR]\PoE Easy Filter Script Editor.exe',
                    None,
                    None,
                    None,
                    'poe.png', #  icon? (None)
                    None,
                    None,
                    'TARGETDIR' #  WkDir
                )]
            }
        },
    },

    executables=[
        Executable(
            targetName='PoE Easy Filter Script Editor.exe',
            script='main.pyw',
            excludes=['tkinter', 'QtSql', 'QtSvg', 'QtTest', 'QtWebKit', 'QtXml'],
            compress=True,
            base=base
        )
    ]
)
