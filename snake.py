import time
from turtle import Turtle, Screen
import os

SPEED = 0.1
MOVE_DISTANCE=20

HEADING_DOWN=270
HEADING_UP=90
HEADING_LEFT=180
HEADING_RIGHT=0

screen = Screen()

class Snake: 

    def __init__(self):
        self.snake_parts = []
        self.createSnake()
        self.head = self.snake_parts[0]

        
    def createSnake(self):
        image = os.path.expanduser("./assets/alja (1).gif")
        screen.addshape(image)
        start_x = 0
        snake_part=Turtle(shape=image)
        snake_part.shapesize(0.5)
        snake_part.penup()
        snake_part.color("blue")
        snake_part.goto(x=start_x,y=0)
        start_x = start_x - 20
        self.snake_parts.append(snake_part)

        for _ in range(2):
            snake_part=Turtle(shape="square")
            snake_part.penup()
            snake_part.color("white")
            snake_part.goto(x=start_x,y=0)
            start_x = start_x - 20
            self.snake_parts.append(snake_part)

    def detectGameOver(self):
        if (self.snake_parts[0].xcor() > 230): return True

        if (self.snake_parts[0].xcor() < -230): return True

        if (self.snake_parts[0].ycor() > 230): return True

        if (self.snake_parts[0].ycor() < -230): return True

        for part in range(1, len(self.snake_parts)-1, 1):
            if self.head.distance(self.snake_parts[part]) < 10:
                return True

        return False

    def moveSnake(self):
        time.sleep(SPEED)

        for snake_index in range(len(self.snake_parts)-1, 0, -1):
            next_snake = self.snake_parts[snake_index - 1]
            self.snake_parts[snake_index].goto(next_snake.xcor(), next_snake.ycor())
                    
        self.snake_parts[0].forward(MOVE_DISTANCE)

    def enlarge(self):
        print("enlarges")
        snake_part=Turtle(shape="square")
        snake_part.penup()
        snake_part.color("white")
        self.snake_parts.append(snake_part)


    def moveUp(self):
        if self.head.heading() != HEADING_DOWN:
            self.head.setheading(HEADING_UP)

    def moveDown(self):
        if self.head.heading() != HEADING_UP:
            self.head.setheading(HEADING_DOWN)

    def moveLeft(self):
        if self.head.heading() != HEADING_RIGHT:
            self.head.setheading(HEADING_LEFT)
    
    def moveRight(self):
        if self.head.heading() != HEADING_LEFT:
            self.head.setheading(HEADING_RIGHT)
