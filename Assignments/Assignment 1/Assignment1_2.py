# Lektion 5, Excercise B 
# Written by Carl Albert Blixt 
# A program that draws the vietnamese_flag
import turtle

def jump(t, x, y): # Sets directions to the tutrtle 
    t.penup()
    t.goto(x,y)
    t.speed(0)
    t.pendown()

def make_turtle(x, y, visible =True): # Sets, position and speed to the turtle. 
    t = turtle.Turtle()
    if visible==False:
        t.hideturtle()
        t.speed(3)
    jump(t, x, y)
    return t

def rectangle(x, y, width, height, color=""): # Draws a rectangle 
    t = make_turtle(x,y) 
    t.fillcolor(color)
    t.begin_fill()
    t.forward(height) # This can be done with a for loop, like in assigment 3, but left the code like the orignal 
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.end_fill()

def vietnamese_flag(x, y, height):# Function that creates the vietnamese flag, uses rectangle and pentagram
    colors = ["red","red","red"]
    width = height/2
    rectangle(x, y, width, height, "red")
    pentagram(x+300, y+230, height*0.3,"yellow") 
    
def pentagram(x, y, side, color): # Creates a pentagram
    t = make_turtle(x,y) # Creates it at (x,y)
    t.hideturtle() 
    t.color(color)
    t.begin_fill()
    t.setheading(252)
    for i in range(5): # For loop to draw a penta gram 
        t.forward(side)
        t.left(180 - 36) # 36 degreees every turn 
    t.end_fill()

# Script, calls the functions to create the flag, 
vietnamese_flag(-300,-150, 600)
turtle.done()













