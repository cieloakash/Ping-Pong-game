import py_compile
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800, height= 600)
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle((-370,0))
r_paddle = Paddle((370,0))
ball = Ball()
score = ScoreBoard()


screen.listen()
screen.onkey(l_paddle.go_up,"Up")
screen.onkey(l_paddle.go_down,"Down")
screen.onkey(r_paddle.go_up,"w")
screen.onkey(r_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed) # slow down the speed of the ball
    screen.update() 
    ball.move()
    # detecting  collosion with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # need to bounce
        ball.bounce_y()

    # detecting collision with the r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340 :
        ball.bounce_x()

    # missing the ball
    if ball.xcor() > 370:
        ball.reset_the_position()
        score.l_point()
    
    if ball.xcor() < -370:
        ball.reset_the_position()
        score.r_point()
    


screen.exitonclick()