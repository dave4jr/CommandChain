#*============================================ #
#*  Author:			Dave Luke Jr
#*  Description:	CommandChain.py
#*============================================ #
import sublime_plugin
import sublime


class CommandChainCommand(sublime_plugin.TextCommand):
	
	def exec_command(self, cmd):
		
		contexts = {
			"window": self.view.window(),
			"app": sublime,
			"text": self.view
		}
		
		if "context" in contexts:
			context = contexts[cmd["context"]]
			
			if "args" in cmd:
				context.run_command(cmd['command'])
			else:
				context.run_command(cmd['command'], cmd['args'])
		else:
			raise Exception("*** CommandChain | Invalid Context: %s | Valid Contexts Include 'window', 'app', or 'text'" % cmd["context"])
		

	def run(self, edit, commands):
		
		for cmd in commands:
			self.exec_command(cmd)
