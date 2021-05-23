from turtle import Turtle


class Score(Turtle):

    # Setting defaults for score object.
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.refresh_score()

    # Updating score when player scores.
    def refresh_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.p1_score, align="center", font=("Helvetica", 60, "normal"))
        self.goto(100, 200)
        self.write(self.p2_score, align="center", font=("Helvetica", 60, "normal"))

    # Incrementing score when player 1 scores.
    def p1_inc(self):
        self.p1_score = self.p1_score + 1
        self.refresh_score()

    # Incrementing score when player 2 scores.
    def p2_inc(self):
        self.p2_score = self.p2_score + 1
        self.refresh_score()

    # Displaying winner when game finishes.
    def display_winner(self):
        self.clear()
        self.goto(0, 0)
        if self.p1_score > self.p2_score:
            self.write("Player 1 is the winner", align="center", font=("Helvetica", 20, "normal"))
        else:
            self.write("Player 2 is the winner", align="center", font=("Helvetica", 20, "normal"))
