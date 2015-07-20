Good day,


You can load and *lazy* edit another [\*.filter](https://www.pathofexile.com/forum/view-thread/1235695) scripts
(**easy** navigation through thousands script lines), just loading it. Comments will be stored.  
*Note:* for correct parsing the structure of your blocks should be like that:  
    Show  
    # some comments  
        BaseType Gem  
        Qualilty > 10  


**Requirements:**  
1. [python3](https://www.python.org/downloads/windows/);  
2. and [PyQt4](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4) for GUI, too;  
3. Win or Linux/Unix.


**Launch bin file:**
Extract zip file, for example, to the $PoEDir\Scripts\FilterEditor.
Double click on *"PoE Easy Filter Script Editor.exe"*, enjoy ;)

**Launch from source _(pythonic way)_:**  
>! Install, copy files main.pyw, config.json, filter_gui.ui and poe.png to  
>! the $PoEDir\Scripts\FilterEditor, for example.  
>! Right-click on main.pyw -> Properties and choose application to run (for me C:\Python34\pythonw.exe).  
>! Done. Easy ;)


**Shortcuts:**  
*Ctrl+O*: Open files (\*.json for previously project or \*.filter for another one);  
*Ctrl+S*: Save project to \*.json file and if something was generated to \*.filter with the same name;  
*Ctrl+A*: Add current block;  
*Ctrl+R*: Update current block;  
*Ctrl+D*: Delete current block;  
*Ctrl+F*: Find all matched words in a generated scripts and underline it by red line;  
*F3*: move to the next match;  
*Ctrl+Enter*: Generate PoE item filter script.
