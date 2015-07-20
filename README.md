Good day,

You can load and simply edit another *.filter scripts
(easy navigation through thousands script lines), just loading it.
Comments will be stored.
Rem.: for correct parsing the structure of your blocks should be like that:
  Show
  # some comments
      BaseType Gem
      Qualilty > 10

Requirements:
1) python3;
2) and PyQt4 for GUI, too;
3) Win or Linux/Unix.

Launch from source:
Install, copy files main.pyw, config.json, filter_gui.ui and poe.png to
the $PoEDir\Scripts\FilterEditor, for example.
Right-click on main.pyw -> Properties and choose application to run (for me C:\Python34\pythonw.exe).
Done. Easy ;)

Launch bin file:
Extract zip file, for example, to the $PoEDir\Scripts\FilterEditor.
Double click on "PoE Easy Filter Script Editor.exe", enjoy ;)

Shortcuts:
Ctrl+O: Open files (*.json for previously project or *.filter for another one);
Ctrl+S: Save project to *.json file and if something was generated to *.filter with the same name.
Ctrl+A: Add current block;
Ctrl+R: Update current block;
Ctrl+D: Delete current block;
Ctrl+F: Find all matched words in a generated scripts and underline it by red line;
F3: move to the next match;
Ctrl+Enter: Generate PoE item filter script.
