## **CommandChain**

This plugin gives you the ability to chain multiple commands into one command bundle and set an associated keymap to the bundle for ease of use.

## Basic Usage
Below are a few example keymaps showing how useful this plugin can be:

1. Save All & Close All
```
{ "keys": ["command+ctrl+alt+x"],
    "command": "run_multiple_commands", "args": {
	    "commands": [
		    { "command": "save_all" },
		    { "command": "close_all" }
		]
	}
}

```

