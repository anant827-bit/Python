import turtle
scr = turtle.Screen()
scr.title("My Canvas")
scr.bgcolor("lightblue")
t=turtle.Turtle()

t.forward(100)
t.left(90)
t.backward(90)

t.penup()
t.goto(0,0)
t.pendown()

t.backward(120)
t.speed(1)

turtle.done()