from turtle import *


cow = Turtle()
screen = Screen()
screen.bgcolor("purple")

cow.color("green")
cow.pensize(4)
cow.speed(4)
cow.shape("turtle")

def drawTriangle():
	for x in range(3):
		cow.forward(80)
		cow.left(120)

for x in range(12):
	drawTriangle()
	cow.left(30)


mainloop()