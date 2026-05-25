import turtle
scr=turtle.Screen()
scr.title("Rectangle & Squares using loops")
scr.bgcolor("pink")

t=turtle.Turtle()

# rectangle without loops
t.forward(100)
t.left(90)
t.forward(80)
t.left(90)
t.forward(100)
t.left(90)
t.forward(80)

t.penup()
t.goto(-100,-100)
t.pendown()

for i in range(2):
    t.forward(100)
    t.left(90)
    t.forward(80)
    t.left(90)

for i in range(4):
    t.forward(200)
    t.right(90)

t.penup()
t.goto(150,150)
t.pendown()

t.circle(8)

t.penup()
t.goto(180,180)
t.pendown()

for i in range(3):
    t.forward(80)
    t.left(120)

turtle.done()