from turtle import Turtle
import pandas


class TextUpdater:

    # Preparing all text displayed on screen.
    def __init__(self):
        self.data = pandas.read_csv("50_states.csv")

        self.display_score = Turtle()
        self.display_score.penup()
        self.display_score.hideturtle()
        self.draw_score(0)

        self.display_state = Turtle()
        self.display_state.penup()
        self.display_state.hideturtle()

        self.display_timer = Turtle()
        self.display_timer.penup()
        self.display_timer.hideturtle()
        self.draw_timer("10:00")

        self.display_lose = Turtle()
        self.display_lose.penup()
        self.display_lose.hideturtle()

        self.display_win = Turtle()
        self.display_win.penup()
        self.display_win.hideturtle()

    # Displays the player's score on screen.
    def draw_score(self, score):
        self.display_score.goto(-250, 280)
        self.display_score.clear()
        self.display_score.write("Score: " + str(score) + "/50", align="center", font=("Helvetica", 20, "normal"))

    # Displays the states that the player has inputted thus far.
    def label_state(self, state):
        state_row = self.data[self.data.state == state]
        x = int(state_row.x)
        y = int(state_row.y)

        self.display_state.goto(x, y)
        self.display_state.write(state, align="center", font=("Helvetica", 7, "normal"))

    # Displays remaining time.
    def draw_timer(self, time):
        self.display_timer.goto(200, 280)
        self.display_timer.clear()
        self.display_timer.write("Time Left: " + time, align="center", font=("Helvetica", 20, "normal"))

    # Displays losing message.
    def draw_lose(self):
        self.display_lose.goto(0,0)
        self.display_lose.write("You have lost.", align="center", font=("Helvetica", 20, "normal"))

    # Displays winning message.
    def draw_win(self):
        self.display_win.goto(0,0)
        self.display_win.write("You have won.", align="center", font=("Helvetica", 20, "normal"))