from turtle import Turtle
import random
COLORS = ['red', 'yellow', 'goldenrod', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def make_car(self) -> None:
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            car = Turtle('square')
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(300, random.randint(-250, 250))
            self.cars.append(car)

    def move_cars(self) -> None:
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self) -> None:
        self.car_speed += MOVE_INCREMENT
