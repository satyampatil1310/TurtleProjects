from turtle import Turtle

class Scorecard(Turtle):
    def __init__(self, position):
        super().__init__()

        self.color("white")
        self.penup()
        self.goto(position)
        self.score = 0
        self.write(arg=f"{self.score}")
        self.shapesize(stretch_len=2, stretch_wid=2)
        self.hideturtle()

    def update(self):
        self.score += 1
        self.clear()
        self.write(arg=f"{self.score}")
