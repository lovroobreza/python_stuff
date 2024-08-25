from turtle import Turtle, Screen
import os

screen = Screen()
HEADING_UP = 90
HEADING_DOWN = 270
HEADING_LEFT = 180
HEADING_RIGHT = 0

FORWARD_MOVE = 20

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        image = os.path.expanduser("./assets/lovro (1).gif")
        screen.addshape(image)

        self.shape(image)
        self.color("green")
        self.goto(x=0, y=-300)

    def didPlayerWin(self):
        if self.ycor() > 300:
            return True
        else:
            return False
        
    def moveDown(self):
        self.setheading(HEADING_DOWN)
        self.forward(FORWARD_MOVE)

    def moveUp(self):
        self.setheading(HEADING_UP)
        self.forward(FORWARD_MOVE)

    def moveLeft(self):
        self.setheading(HEADING_LEFT)
        self.forward(FORWARD_MOVE)

    def moveRight(self):
        self.setheading(HEADING_RIGHT)        
        self.forward(FORWARD_MOVE)
