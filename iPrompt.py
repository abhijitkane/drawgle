#iprompt
import commandParser
PROMPT_BANNER="This is the interactive environment for drawgle. Type help to see a list of commands."
ENDSESSION_BANNER = "--End of interactive drawgle session--"

#func begin
def begin():
	print PROMPT_BANNER
	line=""
	while True:
		line = raw_input(">>")
		if(line=="endsession"):
			break
		commandParser.parse(line);

	print ENDSESSION_BANNER