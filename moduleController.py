#modules.py
COMMANDS = ["new","load","help","line"]
#NOTE: Each module must implement runModule(wholecmd,imagename), and return the name of the file operated on


def isCommand(cmd):
	if(cmd in COMMANDS):
		return True
	else:
		return False

def invokeCommand(wholecmd,imageName):
	cmd=wholecmd.split()[0]
	if not(isCommand(cmd)):
		print "Invalid command '"+cmd+"'. Type help to see a list of commands"
	else:
		importCode = "from modules."+cmd+" import runModule"
		exec importCode

		newImageName = runModule(wholecmd, imageName)
		return newImageName