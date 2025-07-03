import turtle
from math import cos, sin

window = turtle.Screen()
window.bgcolor("#FFFFFF")
window.tracer(0)  # Correct: tracer is called on the Screen object

myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(0)
myPen.pensize(3)
myPen.color("#AA00AA")
myPen.penup()

A = 100
B = 100
a = 3
b = 4
delta = 3.14 / 2
t = 0

for i in range(0, 1000):
    t += 0.01
    # Apply Lissajous Parametric Equations
    x = A * sin(a * t + delta)
    y = B * sin(b * t)

    myPen.goto(x, y)
    myPen.pendown()
    myPen.getscreen().update()


window.mainloop()