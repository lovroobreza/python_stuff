from turtle import Turtle, Screen

timmy = Turtle()

timmy.pencolor("red")

for _ in range(6):
    timmy.pendown()
    timmy.right(60)
    timmy.forward(25)
    timmy.penup()

screen = Screen()
screen.exitonclick()