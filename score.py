from turtle import Turtle

COLOR = "white"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(x=0, y=285)
        self.color(COLOR)
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.write(f"SCORE = {self.score}", align="center", font=('Arial', 13, 'normal'))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align="center", font=('Arial', 20, 'normal'))

    def increase(self):
        self.score += 1
        self.clear()
        self.update_score()

    def decrease(self):
        self.score -= 1
        self.clear()
        self.update_score()