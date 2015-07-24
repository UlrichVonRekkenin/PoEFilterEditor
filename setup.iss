#define Name "PoE Easy Filter Script Editor"
#define Version "1.0.3"
#define Author "UlrichVonRekkenin"
#define Site "https://github.com/UlrichVonRekkenin"
#define Release "https://github.com/UlrichVonRekkenin/PoEFilterEditor/releases"
#define BuildPath ".\build\exe.win32-3.4\"


[Setup]
AppId={{01C19344-6573-4A07-AEF4-87884C682C9C}
AppName={#Name}
AppVersion={#Version}
AppPublisher={#Author}
AppPublisherURL={#Site}
AppUpdatesURL={#Release}
DefaultDirName={userdocs}\My Games\Path of Exile
DefaultGroupName={#Name}
OutputDir=setup
OutputBaseFileName=Setup-{#Name}-{#Version}
Compression=lzma2/max
SolidCompression=yes


[Files]
Source: "{#BuildPath}PoE Easy Filter Script Editor.exe"; DestDir: "{app}"; Flags: ignoreversion touch
Source: "{#BuildPath}filter_gui.ui"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}poe.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}msvcp100.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}MSVCR100.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}python34.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}QtCore4.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}QtGui4.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}PyQt4.Qt.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}PyQt4.QtCore.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}PyQt4.QtGui.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}sip.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}pyexpat.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}library.zip"; DestDir: "{app}"; Flags: ignoreversion


[Dirs]
Name: {code:GetDataDir}; Flags: uninsneveruninstall


[UninstallDelete]
Type: files; Name: "{app}\config.json"


[Icons]
Name: {commondesktop}\PoE Editor; Filename: {app}\{#Name}.exe; WorkingDir: {app}; IconFilename: "{app}\poe.ico";
Name: {group}\{#Name}; Filename: {app}\{#Name}.exe; WorkingDir: {app}; IconFilename: "{app}\poe.ico";
Name: {commonstartup}\{#Name}; Filename: {app}\{#Name}.exe; WorkingDir: {app}; IconFilename: "{app}\poe.ico";
Name: {group}\uninstall; Filename: {app}\unins000.exe; WorkingDir: {app}; IconFilename: "{app}\poe.ico";


[Code]
function GetSystemMetrics(nIndex: Integer): Integer;
  external 'GetSystemMetrics@User32.dll stdcall setuponly';

const
  SM_CXSCREEN = 0;
  SM_CYSCREEN = 1;

var
  DataDirPage: TInputDirWizardPage;


procedure InitializeWizard;
begin

  DataDirPage := CreateInputDirPage(wpSelectDir,
    'Select your PoE *.filter files location', 'Where are your "My Games\Path of Exile" located',
    'Specify the folder to store your *.filter files, then click Next.', False, '');

  DataDirPage.Add('');
  DataDirPage.Values[0] := ExpandConstant('{userdocs}\My Games\Path of Exile');

end;


function GetDataDir(Param: String): String;
var
  json: TArrayOfString;
  dir: string;
begin

  dir := DataDirPage.Values[0];
  StringChangeEx(dir, '\', '\\', True);
  Result := dir;

  SetArrayLength(json, 1);
  json[0] := Format('{"path": "%s", "geo": [%d, %d, %d, %d]}', \
    [Result, \
    GetSystemMetrics(SM_CXSCREEN) div 10, GetSystemMetrics(SM_CYSCREEN) div 10, \
    GetSystemMetrics(SM_CXSCREEN) div 2, Round(0.85*GetSystemMetrics(SM_CYSCREEN))]);

  SaveStringsToFile(ExpandConstant('{app}\config.json'), json, False);

end;
