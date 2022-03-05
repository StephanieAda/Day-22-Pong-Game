from turtle import Screen
from panel import Panel
from ball import Ball
from scoreboard import Scoreboard, Divider

import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)


right_paddle = Panel((350, 0))
left_paddle = Panel((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

ycor = -270

for i in range(0, 8):
    divider = Divider(ycor)
    ycor += 80


screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

print(ball.speed_of_game)
game_is_on = True
while game_is_on:
    time.sleep(ball.speed_of_game)
    screen.update()
    ball.move()

    # detect collision with the wall
    if ball.ycor() < -270 or ball.ycor() > 270:
        ball.bounce_y()

    # detect collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 328 or ball.distance(left_paddle) < 50 and ball.xcor() < -328:
        ball.bounce_x()

    # detect if the right paddle misses the ball
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.add_r_score()
        ball.add_speed()

    # detect if the left paddle misses the ball
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.add_l_score()
        ball.add_speed()

screen.exitonclick()
