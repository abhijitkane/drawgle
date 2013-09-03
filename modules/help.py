#module HELP
#list of in-built commands
from moduleController import COMMANDS

def runModule(wholecmd,imgname):
	print "HELP is running...\n"
	args = wholecmd.split()
	if(len(args)==2):
		#help [cmd]
		commandToCheck = args[1]
		if(commandToCheck in COMMANDS):
			importCode = "from modules."+commandToCheck+" import HELPTEXT"
			exec importCode
			print HELPTEXT+"\n"
			return
		else:
			print "Command "+commandToCheck+" not found"

	print "Supported commands: "
	print COMMANDS

	