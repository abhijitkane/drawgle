#module new
import Image
#syntax: new canvasname width height
def runModule(wholecmd, imageName):
	
	commandSplit = wholecmd.split()
	if commandSplit[0]=="new":

		if not(len(commandSplit)==4):
			print "Command Syntax: new imagename width height"
		else:
			if  (not(commandSplit[2].isdigit())) or (not(commandSplit[3].isdigit())):
				print "width and height must be integers"

			else:
				width = int(commandSplit[2])
				height = int(commandSplit[3])

				#TODO: check width,height are numbers

				canvasname = commandSplit[1]

				newimage = Image.new(mode='RGB',size=(width,height),color=(255,255,255))
				newimage.save("images/"+canvasname+".png")
				return canvasname
	else:
		print "Error"