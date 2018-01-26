# **CommandChain**

This plugin gives you the ability to chain multiple commands into one command bundle and set an associated keymap to the bundle for ease of use. Below are a few example keymaps showing how useful this plugin can be:


#### Save All & Close All
###### Save all tabs and then close all tabs. Useful when you do a find-and-replace that opens 40 tabs up automatically
```
{ "keys": ["command+ctrl+alt+x"],
	"command": "command_chain", "args": {
		"commands": [
			{ "command": "save_all" },
			{ "command": "close_all" }
		]
	}
}

```
   
#### Macros & Plugin Combination
###### Wraps a div in block format by running a user-defined macro
```
{ "keys": ["command+x"],
	"command": "command_chain", "args": {
		"commands": [
			{"command": "run_macro_file", "args": {"file": "res://Packages/User/div-class-wrap.sublime-macro"} }
			,{ "command": "bh_key", "args": { "no_outside_adj": true, "lines": true, "plugin": { "type": ["__all__"], "command": "bh_modules.bracketselect", "args": { "select": "left" } } },"context":"window" }
			,{ "command": "move", "args": {"by": "characters", "forward": true } },{ "command": "move", "args": {"by": "characters", "forward": true } },{ "command": "move", "args": {"by": "characters", "forward": true } },{ "command": "move", "args": {"by": "characters", "forward": true } },{ "command": "move", "args": {"by": "characters", "forward": true } },{ "command": "move", "args": {"by": "characters", "forward": true } },{ "command": "move", "args": {"by": "characters", "forward": true } },{ "command": "move", "args": {"by": "characters", "forward": true } },{ "command": "move", "args": {"by": "characters", "forward": true } },{ "command": "move", "args": {"by": "characters", "forward": true } },{ "command": "move", "args": {"by": "characters", "forward": true } }
		]
	}
}
```
   
#### Gentleman's Way To Convert To Tabs
###### Detect Indentation, convert to tabs and set the tab-width to 4
```
{ "keys": ["command+ctrl+alt+4"],
	"command": "command_chain", "args": {
		"commands": [
			{ "command": "select_all" }
				,{ "command": "detect_indentation" }
				,{ "command": "unexpand_tabs", "args": {"set_translate_tabs": true} }
				,{ "command": "set_setting", "args": {"setting": "tab_size", "value": 4 }
			}
		]
	}
}
```

#### Using With RegReplace
###### Convert a JSON with unicode characters and prettify
```
{ "keys": ["command+ctrl+alt+8"],
		"command": "command_chain", "args": {
			"commands": [
        { "command": "reg_replace", "args": { "replacements": ["format_JSON_1"] } },
        { "command": "reg_replace", "args": { "replacements": ["format_JSON_2"] } },
				{ "command": "reg_replace", "args": { "replacements": ["format_JSON_3"] } },
				{ "command": "reg_replace", "args": { "replacements": ["format_JSON_4"] } },
				{ "command": "pretty_json" },
				{ "command": "select_all" },
				{ "command": "detect_indentation" },
				{ "command": "unexpand_tabs", "args": { "set_translate_tabs": true } },
				{ "command": "set_setting", "args": { "setting": "tab_size", "value": 3 }
      }
		]
	}
}
```


