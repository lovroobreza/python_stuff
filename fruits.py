import math, random
import os
from turtle import Turtle, Screen

screen = Screen()

class Fruit(Turtle): 

    def __init__(self):
        super().__init__()
        self.penup()
        image = os.path.expanduser("./assets/lovro (1).gif")
        screen.addshape(image)

        self.shape(image)
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("white")    
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        x = -220 + math.ceil(random.random()*460)
        y = - 220 + math.ceil(random.random()*460)
        self.goto(x=x,y=y)