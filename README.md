# SublimeTabJumper
**Sublime TabJumper** is a sublime-text-3 plugin that jumping to last active tab or a opened tab quickly. It supports searching all opened tab names in single or multiple groups(`group` in Sublime means split window). When plugin triggered, last active tab name will be seleted.

![SublimeTabJumper](http://i.imgur.com/gFT20V7.gif)

# Installation

* ### Package Control(recommended but not pulished now)
    * Press `Cmd/Ctrl + Shift + P` to open command palette
    * Type `Package Control: Install Package` and press enter
    * Type `TabJumper` and press enter
    * Done

* ### Manual Installation
    * Using Git
        * Open terminal and change the path to Sublime `Packages` directory.(`Preferences > Browse Packages`).
        * Run `git clone https://github.com/lattespirit/SublimeTabJumper.git`.
        * Done.

    * Using zip File
        * Click the `Preferences > Browse Packages…` menu.
        * Download the [Package](https://github.com/lattespirit/SublimeTabJumper/archive/master.zip) file. Unzip and place the whole folder to the path methoned in Step One.
        * Rename the folder to `SublimeTabJumper`.
        * Done.

# Configuration
**SublimeTabJumper** will map `"super/ctrl+k, super/ctrl+j"`(`"super"` means `Command` key in OSX) to trigger the command as default. If this key binding conflicts with the one in your environment, remap it to your favorite one without hesitation.
```json
[
    {
        "keys": ["super/ctrl+k", "super/ctrl+j"], "command": "tab_jumper"
    }
]
```

# Usage
Trigger the keymap metioned above, type the file name which you wish to jump to.

### Suggetion
If Vintage mode is enabled in your Sublime and `enter` key is free, mapping `enter` key to trigger the plugin is highly recommended.
```json
[
    {
        "keys": ["enter"], "command": "tab_jumper",
        "context":
        [
            { "key": "setting.command_mode" }
        ]
    }
]
```