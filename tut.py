from graphics import *
from random import *

win = GraphWin('win', 1000, 1000)
win.setBackground('black')

def mousePolygon(numberOfPoints, r, g, b):
	point = []
	for i in range(0, numberOfPoints):
		pt = win.getMouse()
		pt.setFill('white')
		pt.draw(win)
		
		point.append(pt)
		
	poly = Polygon(point)
	poly.setFill(color_rgb(r, g, b))
	poly.draw(win)
	
for i in range(0, randrange(5, 10)):
	mousePolygon(randrange(3, 8), randrange(255), randrange(255), randrange(255))

win.getMouse()
win.close()
