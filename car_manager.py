from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_cars = Turtle("square")
            new_cars.shapesize(1, 2)
            new_cars.penup()
            new_cars.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_cars.goto(300, random_y)
            self.all_cars.append(new_cars)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def leveling_up(self):
        self.car_speed += MOVE_INCREMENT


