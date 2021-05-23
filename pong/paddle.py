from turtle import Turtle

class Paddle(Turtle):

    # Setting defaults for paddle object.
    def __init__(self, paddle_x, paddle_y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(paddle_x, paddle_y)

    # Moving paddle up when user input detected.
    def move_up(self):
        if not self.ycor() > 230:
            self.goto(self.xcor(), self.ycor() + 20)

    # Moving paddle down when user input detected.
    def move_down(self):
        if not self.ycor() < -230:
            self.goto(self.xcor(), self.ycor() - 20)
