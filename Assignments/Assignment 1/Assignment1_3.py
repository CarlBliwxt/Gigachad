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
    h = t.heading() 
    if (-250 <= t.xcor()  <= 250  and -250 <= t.ycor() <= 250):
        t.setheading(random.randint(h-45, h+45))
    else:
        t.setheading(int(t.towards(0,0)))
    t.forward(random.randint(0,25))

def close(turtle1, turtle2):
    count = 0
    if (turtle1.distance(turtle2) < 50):
        turtle1.write("Close")
        count += 1
    return count
    
#Script 
Length=500 
RANGE_AMOUNT = 150

intervall = [-Length/2, Length/2]
rectangle(-Length/2,-Length/2, Length,  Length, "lightgreen")
turtle1 = make_turtle(random.randint(-Length/2, Length/2), random.randint(-Length/2,Length/2),'blue')
turtle2 = make_turtle(random.randint(-Length/2, Length/2), random.randint(-Length/2,Length/2),'red')

closecounter = 0
for i in range(RANGE_AMOUNT):
    move_random(turtle1)
    move_random(turtle2)
    closecounter += close(turtle1,turtle2)

print(closecounter)
turtle.done() 