from turtle import Turtle
starting_position = [(0, 0), (-20, 0), (-40, 0)]
MAX_DIST = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in starting_position:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(pos)
            self.segments.append(new_segment)

    def add_segment(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.segments[-1].pos())
        self.segments.append(new_segment)

    def move(self):
        for i in range(len(self.segments) - 1, -1, -1):
            if i == 0:
                self.segments[i].fd(MAX_DIST)
            else:
                self.segments[i].goto(self.segments[i - 1].pos())

    def reset(self):
        self.reset()

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
