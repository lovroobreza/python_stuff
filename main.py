from turtle import Turtle, Screen
import random, math


screen = Screen()
screen.setup(width=500, height=500)

colors=["green", "red", "blue", "yellow", "purple"]

offsetY = 500 / 6

turtles=[]

for turtleColor in colors:
    turt = Turtle(shape="turtle")
    turt.penup()
    turt.color(turtleColor)
    turt.goto(y=-250+offsetY, x=-250 + 10)
    offsetY = offsetY + 500 / 6
    turtles.append(turt)

print(turtles)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")

print(user_bet)

race_over  = False
winner = ""

while not race_over: 
    for turtle in turtles:
        turtle.forward(random.random() * 10)
        if turtle.xcor() > 200:
            winner=turtle.color()
            race_over = True

if winner == user_bet:
    screen.textinput("you suck", " haha")
else: 
    screen.textinput("bravo", "haha")
screen.exitonclick()
