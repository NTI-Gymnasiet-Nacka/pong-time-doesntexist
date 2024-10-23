from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# din screen bör vara rektanguljär, ex. 800x600


def main():
    screen = Screen()
    screen.setup(800, 600)
    screen.bgcolor("black")
    screen.title("Pong game")
    screen.tracer(0)
    game_is_on = True
    paddle_1 = Paddle((350,0))
    paddle_2 = Paddle((-350,0))
    

    ball = Ball((0,0))
    #scoreboard = Scoreboard()

    while game_is_on:
        # Update screen and move every tick.
        screen.update()
        time.sleep(0.1)
        screen.listen()
        screen.onkey(paddle_1.moveup, "Up")
        screen.onkey(paddle_2.moveup, "w")
        screen.onkey(paddle_1.movedown, "Down")
        screen.onkey(paddle_2.movedown, "s")
        #paddle_2.moveup()
        ball.moveball()
        screen.listen()
        #screen.onkey(snake.up, "Up")
        #screen.onkey(snake.down, "Down")
        #screen.onkey(snake.left, "Left")
        #screen.onkey(snake.right, "Right")
        

if __name__ == "__main__":
    main()

