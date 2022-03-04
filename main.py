from turtle import Turtle, Screen
from panel import Panel
from ball import Ball

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)


right_paddle = Panel((350, 0))
left_paddle = Panel((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    ball.move()
    if ball.xcor() > 350 or ball.ycor() > 250:
        game_is_on = False

    screen.update()
screen.exitonclick()
