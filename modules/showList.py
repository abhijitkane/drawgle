#module line
import os

HELPTEXT = "Shows the list of saved images"

#syntax: line x1 y1 radius [width [color]]
def runModule(wholecmd, imageName):
	os.system("ls images");

