from turtle import *


cow = Turtle()
screen = Screen()
screen.bgcolor("purple")

cow.color("green")
cow.pensize(4)
cow.speed(4)
cow.shape("turtle")

def drawStar():
	for x in range(5):
		cow.forward(100)
		cow.left(144)

cow.penup()
cow.goto(0,0)
cow.pendown()
drawStar()


cow.penup()
cow.goto(200,0)
cow.pendown()
drawStar()



cow.penup()
cow.goto(-200,0)
cow.pendown()
drawStar()

mainloop()

