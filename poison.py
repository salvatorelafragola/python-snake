from turtle import Turtle
import random


class Poison(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")  # Turtle
        self.penup()  # Turtle
        self.shapesize(stretch_len=1.5, stretch_wid=1.5)  # Turtle
        self.color("purple")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)
