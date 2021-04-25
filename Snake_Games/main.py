from turtle import Screen
import time
from snake import Snake
from food import Food
from scorecard import Scorecard

screen = Screen()
screen.bgcolor("Black")
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.tracer(False, 1000)
is_game_on = True
food = Food()
scorecard = Scorecard()
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if food.distance(snake.head) < 15:
        food.generate_food()
        snake.add_segment()
        scorecard.value += 1
        scorecard.update()
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        snake.reset()
        snake.create_snake()
        if scorecard.highestvalue < scorecard.value:
            scorecard.highestvalue = scorecard.value
            scorecard.update()
        scorecard.value = 0
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:

screen.exitonclick()
