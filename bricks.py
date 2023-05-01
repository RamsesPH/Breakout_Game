from turtle import Turtle
import random


class Brick(Turtle):

    def __init__(self, x, y, width, height, color):
        super().__init__(shape='square')
        self.shapesize(stretch_wid=height/20, stretch_len=width/20)
        self.penup()
        self.goto(x, y)
        self.color(color)
        self.color = color
        print("new Brick added at: ", x, y)

    def draw(self):
        self.stamp()

    def hit(self):
        # self.hideturtle()
        self.clear()
        self.penup()
        self.goto(-1000, -1000)
