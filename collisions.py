import math


def check_collision_brick(ball, brick, scoreboard):
    # Get the coordinates of the ball and brick
    ball_pos = ball.position()
    brick_pos = brick.position()

    # Calculate the distance between the centers of the ball and brick
    distance = math.sqrt((ball_pos[0] - brick_pos[0]) ** 2 + (ball_pos[1] - brick_pos[1]) ** 2)

    # If the distance is less than the sum of the ball and brick radius, there is a collision
    if distance < (ball.shapesize()[0] * 10 + brick.shapesize()[0] * 20):
        scoreboard.increase_score()
        scoreboard.check_score()
        return True
    else:
        return False
