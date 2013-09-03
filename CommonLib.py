def checkInts(*arg):
	for i in arg:
		if ( not (   i.isdigit()  )  ):
			return False;
	return True;