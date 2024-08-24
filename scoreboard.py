import math, random
import os
from turtle import Turtle

class ScoreBoard(Turtle): 

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto( x = 0, y=200)
        self.hideturtle()
        self.updateScoreBoard()

    def addScore(self):
        self.score += 1 
        self.updateScoreBoard() 

    def updateScoreBoard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
