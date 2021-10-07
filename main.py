from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


r_pad = Paddle((350, 0))
l_pad = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(fun=r_pad.up, key='Up')
screen.onkeypress(fun=r_pad.up, key='Up')
screen.onkey(fun=r_pad.down, key='Down')
screen.onkeypress(fun=r_pad.down, key='Down')
screen.onkey(fun=l_pad.up, key='w')
screen.onkeypress(fun=l_pad.up, key='w')
screen.onkey(fun=l_pad.down, key='s')
screen.onkeypress(fun=l_pad.down, key='s')

game = True
while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # horizontal wall collision is this if statement,
    # change 290 to 275?
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # detect collision with pad, pad's x coor is constant, check if ball is at that coor && distance is less than 60
    # by Pythagoras theorem and bounce on x
    if ball.xcor() > 330 and ball.distance(r_pad) < 60:
        ball.bounce_x()
    if ball.xcor() < -330 and ball.distance(l_pad) < 60:
        ball.bounce_x()

    # misses
    if ball.xcor() > 380:
        ball.reset_ball()
        score.update_l()

    if ball.xcor() < -380:
        ball.reset_ball()
        score.update_r()

    # end condition
    MAX_ROUNDS = 5
    if score.l_score > MAX_ROUNDS - 1 or score.r_score > MAX_ROUNDS - 1:
        game = False
        score.game_over()
screen.exitonclick()
