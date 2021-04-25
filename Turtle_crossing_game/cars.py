from turtle import Turtle
import random
color_list = ["red", "green", "blue", "yellow", "black", "pink", "purple", "orange",
               "brown", "violet", "indigo", "cyan", "mustard", "olive", "grey","gold", "silver",
                "dark khaki", "peach", "azure" ]
class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(f"{color_list[b ;m.randint(0, 19)}")
    def colormode(self):
        pass# self.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))



