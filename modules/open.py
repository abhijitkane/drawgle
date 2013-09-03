#module line
import os

HELPTEXT = "Opens the image"

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

	os.system("open images/"+imageName+".png")

