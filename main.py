import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossy Road')
screen.tracer(0)

player = Player()
cm = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.move, key='Up')
screen.onkeypress(fun=player.move, key='w')

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    cm.make_car()
    cm.move_cars()

    # Detect car crash
    for car in cm.cars:
        if car.distance(player) < 20:
            score.game_over()
            game_on = False

    if player.at_finish():
        player.go_start()
        cm.level_up()
        score.level_up()

screen.exitonclick()
