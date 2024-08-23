from turtle import Turtle, Screen
import random

timmy = Turtle()

timmy.pencolor("red")

moves = [0, 90, 180, 270]

timmy.speed("fastest")

for _ in range(600):
    timmy.right(random.choice(moves))
    timmy.forward(20)

screen = Screen()
screen.exitonclick()