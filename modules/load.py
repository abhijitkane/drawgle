#module load
import Image
#syntax: load canvasname
def runModule(wholecmd, imageName):
	
	commandSplit = wholecmd.split()

	if commandSplit[0]=="load":

		if not(len(commandSplit)==2):
			print "Command Syntax: load canvasname"

		else:
			imageToLoad = commandSplit[1]
			try:
				with open('images/'+imageToLoad+'.png','r') as f: pass
			except IOError as e:
				print "File '"+imageToLoad+"'' not found."
				return None


			return imageToLoad
	else:
		print "Error"