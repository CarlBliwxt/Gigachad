import turtle
import random


def jump(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def make_turtle(x, y):
    t = turtle.Turtle()
    t.hideturtle()
    jump(t, x, y)    # Use of the function defined above
    return t

def rectangle(x, y, width, height, color):
    t = make_turtle(x, y)
    t.hideturtle()
    t.fillcolor(color)
    t.begin_fill()
    for dist in [width, height, width, height]:
        t.forward(dist)
        t.left(90)
    t.end_fill()

def tricolore(x, y, h):
    colors = ["blue", "white", "red"]
    w = h/2
    for i in range(3):
        rectangle(x + w*i, y, w, h, colors[i]

def pentagram(x, y, side):
    t = make_turtle(x, y)
    t.hideturtle()
    t.setheading(270 - 36/2)
    for i in range(5):
        t.forward(side)
        t.left(180-36)

def make_turtle(x, y, visible = True):
    t = turtle.Turtle()
    if not visible:
        t.hideturtle()
        t.speed(0)
    jump(t, x, y)
    return t

tricolore(-150, 100, 100)
