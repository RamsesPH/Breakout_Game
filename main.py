# This is my attempt for emulating the Breakout Game ----- Version 1.0
# I am using Turtle as per Pong project day 22 suggested by the project assigner

from turtle import Screen
import random
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from collisions import check_collision_brick
from bricks import Brick

# ---- Variables Area -------


FONT = ('Courier', 18, 'bold')

# defining brick colors by using a list
colors = ["sky blue", "red", "lime", "yellow", "medium turquoise"]

# adding colors weight for the scoring

color_weights = {
    "sky blue": 1,
    "red": 2,
    "lime": 3,
    "yellow": 4,
    "medium turquoise": 5,
}

# ------ / Screen Area / --------

# Todo 1 Create the game screen
screen = Screen()
screen.setup(width=600, height=800)
screen.bgcolor('black')
screen.title('The BreakOut Game by Pedro Hernandez')
screen.tracer(0)  # to eliminate the animation.

# # Creating a brick and registering its shape to the turtle custom list
# screen.register_shape("brick", ((0, 0), (10, 0), (10, 50), (0, 50)))

# Instantiating  objects

ball = Ball()
paddle = Paddle()
scoreboard = Scoreboard()


# ---- / bricks area /-----------

bricks = []

# need to start drawing the wall from the left of the screen, so I have to define wall_width
# and where to start drawing ( start_x ). Range is the number of rows

wall_width = 10 * 60
start_x = -wall_width / 2 + 30

# the range is the number of row I require
for row in range(5):
    for i in range(10):
        index = random.randint(0, len(colors) - 1)
        color = colors[index]
        print(color)
        brick = Brick(start_x + i * 60, row * 30 + 80, 50, 20, color)
        bricks.append(brick)

for brick in bricks:
    brick.draw()


# -----------/ Playing Breakout /-----------------

# Set up a variable to keep track of whether the ball has hit the paddle. If the ball has hit the paddle then
# the variable will be set to True and the screen will get updated. This will make sure the ball bounce towards the bricks
# It will not ripple on  the paddle.

paddle_hit = False

# Set The variable game_on to see if game has not ended
game_on = True
while game_on:

    screen.listen()

    screen.onkey(fun=paddle.go_left, key='Left')
    screen.onkey(fun=paddle.go_right, key='Right')
    # screen.onkey(fun=pause, key="space")

    screen.update()
    ball.move()

    # check for collision with lateral boundary
    if ball.xcor() > 295 or ball.xcor() < -295:
        print("lateral collision")
        ball.bounce_x()
        print("lateral collision")
        screen.update()

    # check for collision with the roof
    if ball.ycor() > 290:
        ball.bounce_y()
        print("roof collision")
        screen.update()

    # check for collision with the floor
    if ball.ycor() < -295:
        game_on = False
        ball.reset_position()
        scoreboard.setposition(x=-10, y=-100)
        scoreboard.write('GAME OVER', align='center', font=('Courier', 24, 'bold'))
        screen.update()

    # check_collision_paddle
    if paddle.distance(ball) < 40:
        if not paddle_hit:
            ball.bounce_y()
            paddle_hit = True
            screen.update()

    # check for collision with bricks
    for brick in bricks:
        if check_collision_brick(ball, brick, scoreboard):
            brick.hit()
            paddle_hit = False

screen.update()
screen.mainloop()