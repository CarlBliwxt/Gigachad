import turtle

def jump(t, positions):
    x = positions[0]
    y = positions[1]
    t.penup()
    t.goto(x, y)
    t.pendown()



cool = -1
turtles = []
positions = [[250, 250], [-250, 250], [-250, -250], [250, -250]]
for i in ["q", "w", "e", "r"]:
    cool = cool + 1
    i = turtle.Turtle()
    jump(i, positions[cool])
    turtles.append(i)
    i.shape("turtle")
    print(turtles)
    if cool == 0:
        i.setheading(-90)
    else:
        angle = i.towards(turtles[cool - 1])
        print(angle)
        i.setheading(angle)


def move(turtles):
    temp = 0
    for i in turtles:
        i.forward(5)
        i.setheading(i.towards(turtles[temp - 1]))
        temp += 1
while turtles[3].distance(turtles[1]) > 10:
    move(turtles)
turtle.done()