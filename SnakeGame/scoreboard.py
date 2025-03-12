from turtle import Turtle
Alignment = "center"
Font = ("Courier", 22, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_screen()

    def update_screen(self):
        self.write((f"Score : {self.score}"), align=Alignment, font=Font)

    def game_over(self):
        self.goto(0,0)
        self.write((f"Game Over"), align=Alignment, font=Font)

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_screen()

