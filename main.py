from turtle import Turtle, Screen
import random, math

timmy = Turtle()
screen = Screen()

timmy.pencolor("red")


moves = [0, 90, 180, 270]

screen.colormode(255)

def change_color():
    R = math.ceil(random.random() * 255)
    B = math.ceil(random.random()* 255)
    G = math.ceil(random.random()* 255) 

    print(R,G,B)

    timmy.pencolor(R, G, B)


timmy.speed("fastest")
timmy.pensize(10)

for _ in range(600):
    change_color()
    timmy.right(random.choice(moves))
    timmy.forward(20)

screen.exitonclick()