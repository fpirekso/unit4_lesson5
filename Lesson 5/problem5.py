from turtle import *


cow = Turtle()
screen = Screen()
screen.bgcolor("purple")

cow.color("green")
cow.pensize(4)
cow.speed(4)
cow.shape("turtle")

for x in range(5):
	cow.forward(50)
	cow.left(144)


mainloop()