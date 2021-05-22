import math
from turtle import Turtle

start_pos = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    # Setting defaults for snake object.
    def __init__(self):
        self.snake_segments = []
        self.snake_creation()

    def snake_creation(self):
        for pos in start_pos:
            self.append_segment(pos)

    # Adding new segment to snake object.
    def append_segment(self, pos):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(pos)
        self.snake_segments.append(new_segment)

    # Calls append_segment when food is collected by snake.
    def growth(self):
        self.append_segment(self.snake_segments[-1].position())

    # Checks distance between head of snake and another point.
    def distance(self, x2, y2):
        return math.sqrt(
            math.pow(self.snake_segments[0].xcor() - x2, 2) + math.pow(self.snake_segments[0].ycor() - y2, 2))

    # Defines movement behavior of snake segments.
    def movement(self):
        for i in range(len(self.snake_segments) - 1, 0, -1):
            next_x = self.snake_segments[i - 1].xcor()
            next_y = self.snake_segments[i - 1].ycor()
            self.snake_segments[i].goto(next_x, next_y)
        self.snake_segments[0].forward(20)

    # Changing directions based on user input (cannot move in opposite direction last moved).
    def move_left(self):
        if self.snake_segments[0].heading() != 0:
            self.snake_segments[0].setheading(180)

    def move_right(self):
        if self.snake_segments[0].heading() != 180:
            self.snake_segments[0].setheading(0)

    def move_up(self):
        if self.snake_segments[0].heading() != 270:
            self.snake_segments[0].setheading(90)

    def move_down(self):
        if self.snake_segments[0].heading() != 90:
            self.snake_segments[0].setheading(270)

    # Check if snake hit wall.
    def wall_collision(self):
        x = self.snake_segments[0].xcor()
        y = self.snake_segments[0].ycor()
        if x > 280 or x < -280 or y > 280 or y < -280:
            return True
        else:
            return False

    # Check if snake obtained food.
    def food_collision(self, food_x, food_y):
        if self.distance(food_x, food_y) < 15:
            return True
        else:
            return False

    # Check if snake collided with itself.
    def self_collision(self):
        x = self.snake_segments[0].xcor()
        y = self.snake_segments[0].ycor()
        for segment in self.snake_segments[1:]:
            if self.distance(segment.xcor(), segment.ycor()) < 15:
                return True
        return False

    # Getter method.
    def get_segments(self):
        return self.snake_segments
