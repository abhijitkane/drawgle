#module line
import Image,ImageDraw
#syntax: line x1 y1 x2 y2
def runModule(wholecmd, imageName):
	#check image exists
	try:
		with open('images/'+imageName+'.png','r') as f: pass
	except IOError as e:
		print "File '"+imageName+"'' not found."
		return None

	args = wholecmd.split()
	if not(len(args)==5):
		print "Correct usage: line x1 y1 x2 y2"
		return None

	x1=args[1]
	y1=args[2]
	x2=args[3]
	y2=args[4]

	if (not(x1.isdigit())) or (not(y1.isdigit())) or (not(x2.isdigit())) or (not(y2.isdigit())):
		print "Coords must be integers"
		return None

	x1=int(x1)
	x2=int(x2)
	y1=int(y1)
	y2=int(y2)

	image = Image.open('images/'+imageName+'.png')
	draw = ImageDraw.Draw(image)
	draw.line((x1,y1,x2,y2), fill="yellow")
	#del draw
	image.save('images/'+imageName+'.png')
