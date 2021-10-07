from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_self(position)

    def create_self(self, coor):
        
        self.shape("square")
        self.color("white")
        self.pu()
        self.speed("fastest")
        self.goto(coor)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
