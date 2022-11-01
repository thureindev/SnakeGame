from turtle import Turtle as T
from constants import BLOCK_SIZE, LIMIT_X_Y

FONT = ('Arial', 16, 'normal')
ALIGNMENT = 'center'
FONT_COLOR = "#FFFFFF"


class Scoreboard(T):
    def __init__(self):
        super().__init__()
        self.score = 0

        self.hideturtle()
        self.penup()
        self.color(FONT_COLOR)
        self.goto(0, LIMIT_X_Y - BLOCK_SIZE)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    def display_gameover(self):
        self.goto(0, 0)
        self.write("GAMEOVER", align=ALIGNMENT, font=FONT)
        self.goto(0, -(BLOCK_SIZE * 3))
        self.write("Press SPACEBAR to play again", align=ALIGNMENT, font=FONT)

    def display_paused(self):
        self.goto(0, 0)
        self.write("PAUSED", align=ALIGNMENT, font=FONT)
        self.goto(0, -(BLOCK_SIZE * 3))
        self.write("Press SPACEBAR to continue", align=ALIGNMENT, font=FONT)
        self.goto(0, LIMIT_X_Y - BLOCK_SIZE)

    def reset_score(self):
        self.score = 0
