from turtle import Turtle
FONT = ("Courier", 16, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.goto(-240, 260)
        self.display()

    def level_up(self) -> None:
        self.level += 1
        self.display()

    def display(self) -> None:
        self.clear()
        self.write(f'Level {self.level}', False, align='center', font=FONT)

    def game_over(self) -> None:
        self.goto(0, 0)
        self.write('GAME OVER', False, align='center', font=('Courier', 40, 'bold'))
