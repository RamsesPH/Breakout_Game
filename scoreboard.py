from turtle import Turtle
# This class defines the Scoreboard.
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.h_score = 0
        self.penup()
        # self.setposition(x=-4, y=340)
        self.pendown()
        self.pencolor('white')
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.penup()
        self.write('ScoreBoard', align='center', font=('Courier', 18, 'bold'))
        self.setposition(x=-10, y=320)
        self.write(f'{self.l_score} | {self.h_score}', False, align='center', font=('Courier', 18, 'bold'))
        self.setposition(x=-10, y=360)

    def increase_score(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def check_score(self):
        if self.l_score > self.h_score:
            self.h_score = self.l_score
        self.clear()
        self.update_scoreboard()
