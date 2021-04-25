from turtle import Turtle
import random
ALIGN = random.randint(0, 360) % 90
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(ALIGN)

    def move(self):
        self.showturtle()
        self.forward(30)
