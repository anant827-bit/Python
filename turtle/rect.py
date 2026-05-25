import turtle
scr=turtle.Screen()
scr.title("Form a rectangle using loop")
scr.bgcolor("yellow")

t=turtle.Turtle()

# square
for i in range(4):
    t.forward(200)
    t.left(90)

t.penup()
t.goto(-100,-100)
t.pendown()

# rectangle
for j in range(2):
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)

turtle.done()