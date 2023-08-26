from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.setheading(90)
        self.penup()
        self.go_start()

    def move(self) -> None:
        self.fd(MOVE_DISTANCE)

    def at_finish(self) -> bool:
        return self.ycor() > FINISH_LINE_Y

    def go_start(self) -> None:
        self.goto(STARTING_POSITION)
