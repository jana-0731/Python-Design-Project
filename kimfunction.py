#function file
import turtle
bob=turtle.Turtle()

def polygon (sides,distance,color):
    angle = 360/sides
    bob.color(color)
    bob.begin_fill()
    for times in range(sides):
        bob.forward(distance)
        bob.left(angle)
        bob.end_fill()

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def star(distance,color):
    bob.color(color)
    bob.begin_fill()
    for times in range(5):
        bob.forward(distance)
        bob.left(144)
        bob.end_fill()
        

def explosion(distance,color):
    bob.color(color)
    for times in range(8):
        bob.forward(distance)
        bob.left(135)

def portal():
    for times in range(60):
        c = (times*4,times*4,times*4)
        polygon(3,125-times*2,c)
        bob.right(92)

