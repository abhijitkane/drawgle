#iprompt
import commandParser
PROMPT_BANNER="This is the interactive environment for drawgle. Type help to see a list of commands."
ENDSESSION_BANNER = "--End of interactive drawgle session--"

#func begin
def begin():
	print PROMPT_BANNER
	line=""
	imagePath=None
	while True:
		line = raw_input("Drawgle>> ")
		if(line=="endsession" or line=='ends'):
			break
		imagePath = commandParser.parse(line,imagePath);

	print ENDSESSION_BANNER