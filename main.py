import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle-crossing game")
screen.bgcolor("white")
player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_cars()
    cars.move_cars()

    # Detect collusion with car.
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    # Reached the top.
    if player.reach_top():
        player.goto_starting()
        cars.leveling_up()
        scoreboard.increase_level()




screen.exitonclick()
