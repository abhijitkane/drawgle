#module line
import Image,ImageDraw
import CommonLib

HELPTEXT = "Prints the name of the canvas that is currently loaded"

#syntax: line x1 y1 radius [width [color]]
def runModule(wholecmd, imageName):
	#check image exists
	if imageName is None:
		print "No file loaded"
		return None

	try:
		with open('images/'+imageName+'.png','r') as f: pass
	except IOError as e:
		print "File '"+imageName+"'' not found."
		return None

	print "File loaded: "+imageName
	return imageName;

