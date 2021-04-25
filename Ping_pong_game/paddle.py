from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        self.goto(position)

    def userup(self):
        y = self.ycor()
        x = self.xcor()
        self.goto(x, y + 50)

    def userdown(self):
        y = self.ycor()
        x = self.xcor()
        self.goto(x, y - 50)