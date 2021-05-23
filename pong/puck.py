from turtle import Turtle


class Puck(Turtle):

    # Setting defaults for puck object.
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.x_velocity = 10
        self.y_velocity = 10
        self.acceleration = 0.03
        self.paddle_cos_handled = False

    # Defining puck movement.
    def move(self):
        self.goto(self.xcor() + self.x_velocity, self.ycor() + self.y_velocity)

    # Defines puck behavior after entering goal.
    def handle_goal_collision(self):
        if self.xcor() > 390:
            self.goto(0, 0)
            self.alter_x_velocity()
            self.acceleration = 0.03
            return "p1 scores"
        elif self.xcor() < -390:
            self.goto(0, 0)
            self.alter_x_velocity()
            self.acceleration = 0.03
            return "p2 scores"

    # Defines puck behavior when hitting wall.
    def handle_wall_collision(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.alter_y_velocity()

    # Defines puck behavior when hit by paddle.
    def handle_paddle_collision(self, paddle_1, paddle_2):
        if not self.paddle_cos_handled and self.distance(paddle_1) < 50 and self.xcor() < -320:
            self.alter_x_velocity()
            self.acceleration = self.acceleration * 0.8
            self.paddle_cos_handled = True

        if not self.paddle_cos_handled and self.distance(paddle_2) < 50 and self.xcor() > 320:
            self.alter_x_velocity()
            self.acceleration = self.acceleration * 0.8
            self.paddle_cos_handled = True

        if -320 < self.xcor() < 320:
            self.paddle_cos_handled = False

    # Reversing puck's x directional movement.
    def alter_x_velocity(self):
        self.x_velocity = self.x_velocity * -1

    # Reversing puck's y directional movement.
    def alter_y_velocity(self):
        self.y_velocity = self.y_velocity * -1
