from turtle import *


cow = Turtle()
screen = Screen()
screen.bgcolor("purple")

cow.color("green")
cow.pensize(4)
cow.speed(4)
cow.shape("turtle")

def drawHex(side):
	for x in range(6):
		cow.forward(side)
		cow.left(60)

drawHex(10)
drawHex(20)
drawHex(30)
drawHex(40)
drawHex(50)
drawHex(60)
drawHex(70)
drawHex(80)
drawHex(90)



mainloop()