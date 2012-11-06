#module line
import Image,ImageDraw
#syntax: line x1 y1 x2 y2 [width [color]]
def runModule(wholecmd, imageName):
	#check image exists
	if imageName is None:
		print "File does not exist. Use new or load first"
		return None

	try:
		with open('images/'+imageName+'.png','r') as f: pass
	except IOError as e:
		print "File '"+imageName+"'' not found."
		return None

	args = wholecmd.split()
	if len(args)<5 or len(args)>7:
		print "Correct usage: line x1 y1 x2 y2 [width [color]]"
		return None

	x1=args[1]
	y1=args[2]
	x2=args[3]
	y2=args[4]
	if(len(args)>5):
		width = args[5]
		fill=args[6]
	else:
		fill="black"
		width=1

	if (not(x1.isdigit())) or (not(y1.isdigit())) or (not(x2.isdigit())) or (not(y2.isdigit())) or (not(width.isdigit())):
		print "Coords must be integers"
		return None

	x1=int(x1)
	x2=int(x2)
	y1=int(y1)
	y2=int(y2)
	width=int(width)

	image = Image.open('images/'+imageName+'.png')
	draw = ImageDraw.Draw(image)
	draw.line((x1,y1,x2,y2), fill,width)
	#del draw
	image.save('images/'+imageName+'.png')
