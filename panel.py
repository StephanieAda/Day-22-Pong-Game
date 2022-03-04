from turtle import Turtle


class Panel(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.setposition(position)
        self.penup()
        self.left(90)
        self.shapesize(1, 5)
        self.color('white')

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)
