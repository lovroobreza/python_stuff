from turtle import Turtle, Screen
import random, math, os
screen = Screen()
class Car():
    def __init__(self):
        self.cars=[]

    def createCar(self):
        print("created car")
        image = os.path.expanduser("./assets/alja (1).gif")
        screen.addshape(image)

        car = Turtle(image)
        car.speed=1.5
        car.penup()
        r = math.ceil(random.random() * 255)
        g = math.ceil(random.random() * 255)
        b = math.ceil(random.random() * 255)
        car.color(r,g,b)
        car.goto(x = 200, y = -250 + random.random() * 500 )
        car.shapesize(stretch_len=2, stretch_wid=0.8)
        #car.goto(x = 50, y = 50 )
        car.setheading(180)
        self.cars.append(car)

    def moveCars(self):
        for car in self.cars:
            car.forward(20)