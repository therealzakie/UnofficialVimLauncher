This file will be outdated pretty soon. If you would like a .app file (like vim.app), go to [this link](macOS_app).

# UnofficialVimLauncher's MacOS Dock Executable

First of all, we are using the ```zsh``` terminal, not the ```bash``` terminal.

Then check your python version. This will be important.

So we need to create a file named ```vim.command``` using ```touch vim.command``` in the ```Applications``` directory (either your user's ```Applications``` directory or the global ```Applications``` directory inside of your disk).

Then we want to edit ```vim.command``` by typing ```vim vim.command```.

Then inside the file, press ```i``` to enter insert mode and then enter:

For python version 3.x

```
#!/bin/zsh
cd UnofficialVimLauncher
python3 main.py
```

For python versions below 3.x

```
#!/bin/zsh
cd UnofficialVimLauncher
python main.py
```

Then rename ```vim.command``` to ```vim.app```. This will not make the app functional.

Place ```vim.app``` in your dock.

Then finally rename ```vim.app``` back to ```vim.command```. This will keep it in the dock.
