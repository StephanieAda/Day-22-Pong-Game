from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.shape('circle')
        self.x_move = 10
        self.y_move = 10
        self.speed_of_game = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setx(new_x)
        self.sety(new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.bounce_y()
        self.bounce_x()
        self.setpos(0, 0)

    def add_speed(self):
        self.speed_of_game -= 0.01
        print(self.speed_of_game)
        if self.speed_of_game = 0.03:
            self.speed_of_game = 0.03
