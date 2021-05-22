from turtle import Turtle
import random

shapes = ["circle", "square", "triangle"]
colors = ["red", "blue", "yellow"]


class Food:

    # Setting defaults for food object.
    def __init__(self, segment_list):
        self.shape = ""
        self.color = ""
        self.x = 0
        self.y = 0
        self.new_food = None
        self.randomize(segment_list)

    # Drawing food on screen after randomizing location, color, and shape.
    def randomize(self, segment_list):
        if self.new_food is not None:
            self.new_food.goto(-1000, -1000)
        self.shape = random.choice(shapes)
        self.color = random.choice(colors)

        while True:
            self.x = random.randint(-260, 260)
            self.y = random.randint(-260, 260)
            no_conflicts = True
            for seg in segment_list:
                x = seg.xcor()
                y = seg.ycor()
                if not (abs(self.x - x) > 20 and abs(self.y - y) > 20):
                    no_conflicts = False
            if no_conflicts:
                break

        self.new_food = Turtle(self.shape)
        self.new_food.penup()
        self.new_food.color(self.color)
        self.new_food.goto(self.x, self.y)

    # Getter methods.
    def get_food(self):
        return self.new_food

    def get_food_x(self):
        return self.x

    def get_food_y(self):
        return self.y
