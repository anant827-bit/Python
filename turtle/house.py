import turtle
scr=turtle.Screen()
scr.title("Constructing a home using turtle")
scr.bgcolor("lightblue")
t=turtle.Turtle()

t.penup()
t.goto(-100,-100)
t.pendown()

# lower door
for i in range(2):
    t.forward(100)
    t.right(90)
    t.forward(150)
    t.right(90)

# upper triangle
t.left(60)
t.forward(100)
t.right(120)
t.forward(100)
# pointer at (0,-100)

# lower second half
t.left(60)
t.forward(300)
t.right(90)
t.forward(150)
t.right(90)
t.forward(300)

t.penup()
t.goto(300,-100)
t.pendown()

# upper second half
t.right(90)
t.forward(86.6)
t.left(90)
t.forward(349)

t.penup()
t.goto(-50,-60)
t.pendown()

# circle 
t.circle(8)

t.penup()
t.goto(-75,-250)
t.pendown()

t.right(90)
t.forward(75)
t.right(90)
t.forward(50)
t.right(90)
t.forward(75)

turtle.done()