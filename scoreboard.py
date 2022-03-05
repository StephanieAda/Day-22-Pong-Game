from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.current_scores()

    def current_scores(self):
        self.setpos(-60, 220)
        self.write(self.l_score, False, 'center', font=('Courier', 60, 'bold'))

        self.setpos(60, 220)
        self.write(self.r_score, False, 'center', font=('Courier', 60, 'bold'))

    def add_l_score(self):
        self.l_score += 1
        self.clear()
        self.current_scores()

    def add_r_score(self):
        self.r_score += 1
        self.clear()
        self.current_scores()


class Divider(Turtle):

    def __init__(self, ycor):
        super().__init__()
        self.penup()
        self.color('white')
        self.sety(ycor)
        self.shape('square')
        self.shapesize(1.5, 0.3)
