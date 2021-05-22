from turtle import Screen
import time
from score import Score
from snake import Snake
from food import Food

# Setting up game window.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

# Setting up objects in game.
snake_instance = Snake()
food_instance = Food(snake_instance.get_segments())
score = Score()

# Accepting player input.
screen.listen()
screen.onkeypress(snake_instance.move_left, "Left")
screen.onkeypress(snake_instance.move_right, "Right")
screen.onkeypress(snake_instance.move_up, "Up")
screen.onkeypress(snake_instance.move_down, "Down")

# Game loop
run = True
while run:
    screen.update()
    time.sleep(0.05)
    snake_instance.movement()
    if snake_instance.wall_collision():
        run = False
    if snake_instance.self_collision():
        run = False
    if snake_instance.food_collision(food_instance.get_food_x(), food_instance.get_food_y()):
        food_instance.randomize(snake_instance.get_segments())
        snake_instance.growth()
        score.inc_score()
        score.update_score_counter()

screen.bye()
