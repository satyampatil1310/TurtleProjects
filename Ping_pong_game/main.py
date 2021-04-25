from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scorecard import Scorecard

screen = Screen()
screen.setup(width=1000, height=700)
screen.bgcolor("Black")
border = Turtle()
border.hideturtle()
border.color("White")
border.penup()
border.goto(0, 300)
border.setheading(270)
screen.tracer(False)
while border.ycor() != -300:
    border.pendown()
    border.fd(10)
    border.penup()
    border.fd(10)

rpaddle = Paddle((475, 0))
lpaddle = Paddle((-480, 0))
ball = Ball()
rscore = Scorecard((20, 330))
lscore = Scorecard((-20, 330))

screen.listen()
screen.onkey(rpaddle.userup, "Up")
screen.onkey(rpaddle.userdown, "Down")
screen.onkey(lpaddle.userup, "w")
screen.onkey(lpaddle.userdown, "s")
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    ball.hideturtle()
    if ball.ycor() > 340 or ball.ycor() < -340:
        ball.setheading(-ball.heading())

    if ball.distance(rpaddle) < 60 and ball.xcor() > 460:
        ball.setheading(180 - ball.heading())
        rscore.update()

    if ball.distance(lpaddle) < 60 and ball.xcor() < -460:
        ball.setheading(180 - ball.heading())
        lscore.update()

    if ball.xcor() > 480 or ball.ycor() < -480:
        game_on = False
    ball.move()
screen.exitonclick()




