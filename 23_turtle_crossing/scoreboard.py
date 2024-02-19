from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    level = 1

    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.goto(-240, 270)
        self.write("Level: " + str(self.level), align="center", font=("Courier", 15, "normal"))

    def level_up(self):
        self.clear()
        self.level += 1
        self.write("Level: " + str(self.level), align="center", font=("Courier", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 15, "normal"))
