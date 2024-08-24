from turtle import Screen
from snake import Snake
from fruits import Fruit

screen = Screen()
screen.setup(width=500, height=500)
screen.title("Snakez")
screen.bgcolor("black")

snake = Snake()
fruit = Fruit()


screen.listen()
screen.onkey(snake.moveDown, "Down")
screen.onkey(snake.moveLeft, "Left")
screen.onkey(snake.moveUp, "Up")
screen.onkey(snake.moveRight, "Right")

def game():
    screen.update()
    screen.tracer(0)
    game_over = False
    while not game_over:
        snake.moveSnake()
        screen.update()
        game_over = snake.detectGameOver()
        if snake.head.distance(fruit) < 25:
            snake.enlarge()
            fruit.refresh()

    

game()

screen.exitonclick()
