from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Ping-Pong")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.move_up,"Up")
screen.onkeypress(r_paddle.move_down,"Down")
screen.onkeypress(l_paddle.move_up,"w")
screen.onkeypress(l_paddle.move_down,"s")

is_game_on=True
while is_game_on:
  time.sleep(ball.move_speed)
  screen.update()
  ball.move()
  #Detect collision with wall
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

  #detect collision with paddle
  if ball.distance(r_paddle) < 50 and ball.xcor() >320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
   ball.bounce_x()
   
  #detect when right paddle misses
  if ball.xcor() > 380:
      ball.reset_position()
      scoreboard.l_point()
      scoreboard.update()
    
  #detect when lrft paddle misses
  if ball.xcor() < -380:
    ball.reset_position()
    scoreboard.r_point()
    scoreboard.update()
    
screen.exitonclick()

