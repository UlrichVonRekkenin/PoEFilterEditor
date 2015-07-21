<!-- TOC depth:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Fast way](#fast-way)
- [Pythonic way (run from source)](#pythonic-way-run-from-source)
	- [Requirements](#requirements)
	- [Launch from source](#launch-from-source)
- [Shortcuts](#shortcuts)


# PoE Filter Lazy Editor

Good day,


You can open and *lazy* edit another [\*.filter](https://www.pathofexile.com/forum/view-thread/1235695) for [PoE](http://pathofexile.com/) loot scripts
(**easy** navigation through thousands script lines), just opening it. Comments will be stored.  
**Note:** for correct parsing the structure of your script blocks should be like that:  

    Show  
    # Alert when drop gem with >q10  
        BaseType Gem  
        Qualilty > 10
        PlayAlertSound 1 100  


# Fast way
Download and install the *"PoE Easy Filter Script Editor-version-win32.msi"*. Specify the installation directory, for example `$PoEInstallDir\Scripts\PoEFilterEditor`.  
Note: Check what is your script filter directory, I mean the prefix for `[My] Documents` folder (`C:\Users\PoEUser\**My Documents**\My Games\Path of Exile`). In a filter guides it\`s the *My Documents* but on my Win8.1 it a simple *Documents*  Write down the correct to field in the `config.json` file `docPath`:

    {"docPath": "Documents", "Geometry": [250, 100, 1000, 850]}


# Pythonic way (run from source)
## Requirements
1. [python3](https://www.python.org/downloads/windows/);
2. and [PyQt4](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4) for GUI, too;
3. Win or Linux/Unix.


## Launch from source
Copy files `main.pyw`, `config.json`, `filter_gui.ui` and `poe.png` to the `$PoEInstallDir\Scripts\PoEFilterEditor`, for example. Right-click on `main.pyw` -> Properties and choose application to run (for me `C:\Python34\pythonw.exe`). Done. Easy ;)


# Shortcuts
**Ctrl+O**: Open files (\*.json for previously project or \*.filter for another one);
**Ctrl+S**: Save project to \*.json file and if something was generated to \*.filter with the same name;
**Ctrl+A**: Add current block;
**Ctrl+R**: Update current block;
**Ctrl+D**: Delete current block;
**Ctrl+F**: Find all matched words in a generated scripts and underline it by red line;
**F3**: move to the next match;
**Ctrl+Enter**: Generate PoE item filter script.
