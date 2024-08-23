from turtle import Turtle, Screen

timmy = Turtle()

timmy.pencolor("red")

t=3
for _ in range(10):
    for _ in range(t):
        timmy.pendown()
        timmy.right(360 / t)
        timmy.forward(25 + t * 5)
        timmy.penup()
    t = t +1


screen = Screen()
screen.exitonclick()