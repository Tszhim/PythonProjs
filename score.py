from turtle import Turtle


class Score:

    # Setting defaults for score object.
    def __init__(self):
        self.points = 0
        self.color = "white"
        self.location_x = 0
        self.location_y = 270
        self.new_score = None
        self.update_score_counter()

    # Writing score on screen.
    def update_score_counter(self):
        self.new_score = Turtle()
        self.new_score.score = self.points
        self.new_score.color(self.color)
        self.new_score.penup()
        self.new_score.goto(self.location_x, self.location_y)
        self.new_score.hideturtle()
        self.new_score.write(f"Score: {self.new_score.score}", align="center", font=("Helvetica", 20, "normal"))

    # Incrementing score.
    def inc_score(self):
        self.points = self.points + 1
        self.new_score.score = self.points
        self.new_score.clear()
