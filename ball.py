from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        # self.hideturtle()
        self.speed('slow')
        self.color('white')
        self.penup()
        self.shape('circle')

    def move(self):
        # self.setpos(350, 250)
        new_x = self.xcor() + 30
        new_y = self.ycor() + 20
        self.setx(new_x)
        self.sety(new_y)
