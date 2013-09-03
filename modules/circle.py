#module line
import Image,ImageDraw
import CommonLib

HELPTEXT = "Draws a circle on the canvas. Usage: circle x0 y0 radius [width [color]]\nx0,y0: coordinates of the center\nradius: radius\nwidth: width of the border\ncolor: color of fill"

#syntax: line x1 y1 radius [width [color]]
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
	if len(args)<4 or len(args)>6:
		print "Correct usage: circle x0 y0 radius [width [color]]"
		return imageName

	x1=args[1]
	y1=args[2]
	radius=args[3]

	if(len(args)>4):
		width = args[4]
		fill=args[5]
	else:
		fill="black"
		width=1

	#if (not(x1.isdigit())) or (not(y1.isdigit())) or (not(radius.isdigit())) or (not(width.isdigit())):
	if( not CommonLib.checkInts(x1 , y1, radius, width)):
		print "Coords must be integers"
		return imageName

	x1=int(x1)
	y1=int(y1)
	radius=int(radius)
	width=int(width)

	image = Image.open('images/'+imageName+'.png')
	draw = ImageDraw.Draw(image)
	draw.ellipse((x1-radius, y1-radius, x1+radius, y1+radius), fill, width)
	
	#del draw
	image.save('images/'+imageName+'.png')
	return imageName
