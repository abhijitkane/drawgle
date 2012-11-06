#fileParser module
import commandParser
#beginParsing - takes 1 argument

def beginParsing(filename):
	#check file exists
	try:
		with open(filename) as f: pass
	except IOError as e:
		print "File "+filename+" not found."

	#start parsing file
	for line in open(filename,'r').readlines():
		commandParser.parse(line)
	