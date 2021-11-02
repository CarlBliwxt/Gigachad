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
    t.hideturtle()
    t.begin_fill()
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.end_fill()

def vietnamese_flag(x, y, height):
    colors = ["red","red","red"]
    width = height/2
    rectangle(x, y, width, height, "red")
    pentagram(x+300, y+230, height*0.3,"yellow") 
    



def pentagram(x, y, side, color):
    t = make_turtle(x,y) # Creates it at (x,y)
    t.speed(0) 
    t.hideturtle() 
    t.color(color)
    t.begin_fill()
    
    t.setheading(252)
    for i in range(5):
        t.forward(side)
        t.left(180 - 36)
    t.end_fill()

def star(x, y, height, color):
    distans=120
    for i in range(amount):
        pentagram(x, y, distans, color)
        x=x+distans

vietnamese_flag(-300,-150, 600)
turtle.done()













