# Lektion 5, Excercise A 
# Written by Carl Albert Blixt 
# A program that draws the French flag and pentagons, with turtles 
import turtle
import random

def jump(t, x, y): # Sets the direcition of the turtle
    t.penup()
    t.goto(x,y)
    t.speed(0)
    t.pendown()

def make_turtle(x, y, visible =True): # Creates a turtle and sets speed 
    t = turtle.Turtle()
    if visible==False:
        t.hideturtle()
        t.speed(0)
    jump(t, x, y)
    return t

def random_turtle(side=500): # Creates a random turtle inside a square
    t = make_turtle(random.randint(-side/2, side/2),
                    random.randint(-side/2,side/2))
    t.setheading(random.randint(0, 359)) 
     

def rectangle(x, y, width, height, color=""): # Draws a recttangle 
    t = make_turtle(x,y) 
    t.fillcolor(color)
    t.hideturtle()
    t.begin_fill()
    t.forward(width) # Can be done with for loop, like assigment 3. 
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.end_fill()

def tricolore(x, y, h):
    colors = ["blue", "white", "red"] 
    w = h/2
    for i in range(3):
        rectangle(x + w*i, y, w, h, colors[i]) 


def pentagram(x, y, side, color): # Creates a pentagram 
    t = make_turtle(x,y) # Creates it at (x,y)
    t.color(color)
    t.speed(0) 
    t.begin_fill()
    t.hideturtle() 
    t.setheading(252)
    for i in range(5):
        t.forward(side)
        t.left(180 - 36)
    t.end_fill()

def generator(x, y, amount, color): # Uses the pentagram to create amount, and what color
    distans=120
    for i in range(amount):
        pentagram(x, y, distans, color)
        x=x+distans


tricolore(-200, -50, 250)
generator(-240, 375, 5, "green")
generator(-240, -130, 5, "green")

turtle.done()