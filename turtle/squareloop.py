import turtle
scr=turtle.Screen()
scr.title("Star using turtle")
scr.bgcolor("lightgreen")
t=turtle.Turtle()
t.color("black")

def square(len):
    for i in range(4):
        t.forward(len)
        t.left(90)
        len=len+5

square(20)
square(40)
square(60)
square(80)
square(100)

turtle.done()