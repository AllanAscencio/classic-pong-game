from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    # Paddle Movement

    def go_up(self):
        new_y = self.ycor() + 50  # Getting the current y-coordinated of the left paddle
        self.goto(self.xcor(), new_y)  # Updating the y-coordinated of the paddle

    # Function to move the left paddle down
    
    def go_down(self):
        new_y = self.ycor() - 50  # Getting the current y-coordinated of the left paddle
        self.goto(self.xcor(), new_y)  # Updating the y-coordinated of the paddle

