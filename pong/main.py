import time
from turtle import Screen
from paddle import Paddle
from puck import Puck
from score import Score

# Setting up screen.
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Creating up game objects.
p1_paddle = Paddle(-350, 0)
p2_paddle = Paddle(350, 0)
score = Score()
puck = Puck()

# Accepting user input.
screen.onkeypress(p1_paddle.move_up, "w")
screen.onkeypress(p1_paddle.move_down, "s")
screen.onkeypress(p2_paddle.move_up, "Up")
screen.onkeypress(p2_paddle.move_down, "Down")
screen.listen()

# Game loop
run = True
while run:
    time.sleep(puck.acceleration)
    screen.update()
    puck.move()

    puck.handle_wall_collision()
    point_winner = puck.handle_goal_collision()
    puck.handle_paddle_collision(p1_paddle, p2_paddle)
    if point_winner == "p1 scores":
        score.p1_inc()
    elif point_winner == "p2 scores":
        score.p2_inc()

    if score.p1_score == 10 or score.p2_score == 10:
        score.display_winner()
        run = False

screen.exitonclick()
