from turtle import Screen
import time

from player import Player
from car import Car

screen = Screen()
screen.setup(width=500, height=700)
screen.title("crossy roads")
screen.bgcolor("black")

screen.tracer(0)
screen.colormode(255)
player = Player()
car = Car()

screen.listen()
screen.onkey(player.moveDown, "Down")
screen.onkey(player.moveLeft, "Left")
screen.onkey(player.moveUp, "Up")
screen.onkey(player.moveRight, "Right")

def playerLost():
    player_lost = False
    for c in car.cars:
        if player.distance(c) < 20:
            player_lost=True
            break
    return player_lost

def game():
    screen.update()
    game_over = False
    player_won = False

    runs = 0
    
    while (not game_over) and (not player_won):      
        runs += 1
        time.sleep(0.1)
        if runs % 2 == 0:
            car.createCar()
        car.moveCars()
        screen.update()

        game_over = playerLost()
        player_won = player.didPlayerWin()

    if player_won:
        print("gg")
    if game_over:
        print("sucks to suck")


game()

screen.exitonclick()
