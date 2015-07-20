@echo off

py -3 setup.py build_exe

REM

mkdir minimal
cd build\exe.win32-3.4

move msvcp100.dll ..\..\minimal
move MSVCR100.dll ..\..\minimal
move python34.dll ..\..\minimal
move QtCore4.dll ..\..\minimal
move QtGui4.dll ..\..\minimal
move PyQt4.Qt.pyd ..\..\minimal
move PyQt4.QtCore.pyd ..\..\minimal
move PyQt4.QtGui.pyd ..\..\minimal
move sip.pyd ..\..\minimal
move pyexpat.pyd ..\..\minimal
move library.zip ..\..\minimal

move "PoE Easy Filter Script Editor.exe" ..\..\minimal
move filter_gui.ui ..\..\minimal
move config.json ..\..minimal

cd ..\..

pause
