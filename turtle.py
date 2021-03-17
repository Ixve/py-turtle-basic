# CONTROLS:
# Left click changes colors.
# Right click stamps the arrow.
# Q to raise the pen up.
# E to put the pen down.
# Short controls: WASD
# Long controls: Arrow keys
# Spacebar to clear the screen
# F to see the turtle's current position (x, y)

import turtle
import random
from turtle import *

tu = turtle.Turtle()
tu.speed(0)
tu.width(5)

colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black']

def up():
    tu.setheading(90)
    tu.forward(50)

def down():
    tu.setheading(270)
    tu.forward(50)

def left():
    tu.setheading(180)
    tu.forward(50)

def right():
    tu.setheading(0)
    tu.forward(50)

def leftclick(x,y):
    tu.color(random.choice(boje))

def rightclick(x,y):
    tu.stamp()

def penup():
    tu.penup()

def pendown():
    tu.pendown()

def longUp():
    tu.setheading(90)
    tu.forward(100)

def longDown():
    tu.setheading(270)
    tu.forward(100)

def longLeft():
    tu.setheading(180)
    tu.forward(100)

def longRight():
    tu.setheading(0)
    tu.forward(100)

def clear():
    tu.clear()

def position():
    print("Current Turtle's position: ", tu.pos())
        
turtle.listen()

turtle.onscreenclick(leftclick, 1)
turtle.onscreenclick(rightclick, 3)

turtle.onkey(up, 'w')
turtle.onkey(left, 'a')
turtle.onkey(down, 's')
turtle.onkey(right, 'd')
turtle.onkey(longUp, 'Up')
turtle.onkey(longLeft, 'Left')
turtle.onkey(longDown, 'Down')
turtle.onkey(longRight, 'right')
turtle.onkey(clear, 'space')
turtle.onkey(position, 'f')

turtle.mainloop()
