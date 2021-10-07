from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.change()

    def change(self):
        self.clear()
        self.goto(-100, 220)
        self.write(f"{self.l_score}", move=False, align="center", font=("Arial", 50, "normal"))
        self.goto(100, 220)
        self.write(f"{self.r_score}", move=False, align="center", font=("Arial", 50, "normal"))

    def update_l(self):
        self.l_score += 1
        self.change()

    def update_r(self):
        self.r_score += 1
        self.change()

    def game_over(self):
        if self.l_score > self.r_score:
            self.clear()
            self.goto(0, 0)
            self.write(f"LEFT WINS WITH {self.l_score} POINTS!", move=False, align="center",
                       font=("Arial", 38, "normal"))
        else:
            if self.l_score > self.r_score:
                self.clear()
                self.goto(0, 0)
                self.write(f"RIGHT WINS WITH {self.r_score} POINTS!", move=False, align="center",
                           font=("Arial", 38, "normal"))
