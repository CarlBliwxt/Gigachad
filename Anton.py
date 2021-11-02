# Lektion 5, Part 3 
# Written by Carl Albert Blixt 
# A program that does dizzy things
import turtle
import random


def jump(t, x, y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def make_turtle(x, y, color ):
    t = turtle.Turtle()
    t.color(color)
    jump(t, x, y)    # Use of the function defined above
    return t


def rectangle(x, y, width, height, color=""):
    t = make_turtle(x,y,color) 
    t.fillcolor(color)
    t.speed(0)
    t.hideturtle()
    t.begin_fill()
    for distance in [height,width,height,width]:
        t.forward(distance)
        t.left(90)
    t.end_fill()

def move_random(t):
    #Måste ha en input
    h = int(t.heading())
    if (-250 <= t.xcor()  <= 250  and -250 <= t.ycor() <= 250):
        t.setheading(random.randint(h-45, h+45))
    else:
        t.setheading((t.towards(0,0)))
    t.forward(random.randint(0,25))

#Script 
Length=500 
intervall = [-Length/2, Length/2]
rectangle(-Length/2,-Length/2, Length,  Length, "lightgreen")
x = make_turtle(random.randint(-Length/2, Length/2), random.randint(-Length/2,Length/2),'blue')
for i in range(500):
    move_random(x)
turtle.done()