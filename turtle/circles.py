import turtle
scr=turtle.Screen()
scr.title("Star using turtle")
scr.bgcolor("white")
t=turtle.Turtle()
t.color("darkblue")

# def circle(l):
#     for i in range(3):
#         t.circle(l)
#         l=l+10
#         t.setposition(l,0)


t.circle(50)

t.penup()
t.setposition(-120,0)
t.pendown()

t.color("black")
t.circle(50)

t.penup()
t.setposition(120,0)
t.pendown()

t.color("red")
t.circle(50)

t.penup()
t.setposition(60,60)
t.pendown()

t.color("yellow")
t.circle(50)

t.penup()
t.setposition(-60,60)
t.pendown()

t.color("green")
t.circle(50)

turtle.exitonclick()