from turtle import Turtle


class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.value = 0
        self.highestvalue = 0
        self.write(arg=f"Score ={self.value}  HighestScore = {self.highestvalue}", align="center")


    def update(self):
        self.clear()
        self.write(arg=f"Score ={self.value}  HighestScore = {self.highestvalue}", align="center")



