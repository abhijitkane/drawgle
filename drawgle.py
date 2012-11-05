#drawgle.py

import sys
#either execute interactive environment, or parse file
import fileParser
import iPrompt

if __name__ != "__main__":
	exit()
else:
	if(len(sys.argv)==2):
		#have to parse the file
		fileParser.beginParsing(sys.argv[1])
	elif(len(sys.argv)==1):
		#enter interactive mode
		iPrompt.begin()
	else:
		print("Invalid number of parameters. Usage: drawgle [programFile1]")
