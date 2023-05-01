from turtle import Turtle


# This creates a ball  with the given char and allows it to move and bounce
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.shapesize(0.5)
        self.penup()
        self.goto(0, -100)
        self.setheading(270)
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        # self.move_speed *= 0.1

    def reset_position(self):
        self.goto(0, 100)
        self.bounce_x()


