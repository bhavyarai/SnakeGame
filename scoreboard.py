from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Ariel', 12, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=270)
        self.update_score()

    def update_score(self):
        self.update_high_score()
        self.write(arg=f"Score: {self.score}   High Score: {self.high_score}", font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", font=FONT, align=ALIGNMENT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def update_high_score(self):
        print(self.score, self.high_score)
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")