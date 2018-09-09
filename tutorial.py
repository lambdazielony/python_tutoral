from graphics import *

class Ball:
	def __init__(self, startx, starty, radius):
		self.x = startx
		self.y = starty
		self.r = radius
	def setX(self, xx):
		self.x = xx

win = GraphWin("Ball", 800, 600)
win.setBackground('black')

bal = Ball(100, 100, 20)
i = 0;

while True:
	
	circle = Circle(Point(bal.x, bal.y), bal.r)
	circle.setFill('yellow')

	bal.setX(i)
	i+=1

	circle.draw(win)

	win.getMouse()	
	win.close()

