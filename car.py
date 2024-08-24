from turtle import Turtle
import random, math

class Car():
    def __init__(self):
        self.cars=[]

    def createCar(self):
        print("created car")
        car = Turtle(shape="square")
        car.speed=1.5
        car.penup()
        r = math.ceil(random.random() * 255)
        g = math.ceil(random.random() * 255)
        b = math.ceil(random.random() * 255)
        car.color(r,g,b)
        car.goto(x = 200, y = -250 + random.random() * 500 )
        car.shapesize(stretch_len=2, stretch_wid=1)
        #car.goto(x = 50, y = 50 )
        car.setheading(180)
        self.cars.append(car)

    def moveCars(self):
        for car in self.cars:
            car.forward(20)