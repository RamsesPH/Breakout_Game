from turtle import Turtle

# "This class will create a paddle(magenta stretched square) and allow horizontal movement"

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=5, stretch_wid=0.4)
        self.color('magenta')
        self.penup()
        self.goto(-40, -240)

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())


