#modules.py
COMMANDS = ["new","help"]

def isCommand(cmd):
	if(cmd in COMMANDS):
		return True
	else:
		return False

def invokeCommand(wholecmd):
	cmd=wholecmd.split()[0]
	if not(isCommand(cmd)):
		print "Invalid command '"+cmd+"'. Type help to see a list of commands"
	else:
		importCode = "from modules."+cmd+" import runModule"
		exec importCode
		runModule(wholecmd)