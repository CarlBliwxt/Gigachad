# Lektion 5, Excercise B 
# Written by Carl Albert Blixt 
# A program that draws the vietnamese_flag
import turtle

#skärm för outputen

def jump(t, x, y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def make_turtle(x, y, visible =True):
    t = turtle.Turtle()
    if visible==False:
        t.hideturtle()
        t.speed(0)
    jump(t, x, y)
    return t

def rectangle(x, y, width, height, color=""):
    t = make_turtle(x,y) 
    t.fillcolor(color)
    t.speed(0)
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.end_fill()

def vietnamese_flag(x, y, height):
    colors = ["red", "yellow"]
    w = h/2
    for i in range(2):
        rectangle(x + w*i, y, w, h, colors[i]) 


def pentagram(x, y, side, color):
    t = make_turtle(x,y) # Creates it at (x,y)
    t.speed(0) 
    t.begin_fill()
    t.hideturtle() 
    t.setheading(252)
    for i in range(5):
        t.forward(side)
        t.left(180 - 36)
    t.end_fill()

def generator(x, y, amount, color):
    distans=120
    for i in range(amount):
        pentagram(x, y, distans, color)
        x=x+distans


tricolore(-200, -50, 250)
generator(-240, 375, 5, "default")
generator(-240, -130, 5, "default")

turtle.done()













