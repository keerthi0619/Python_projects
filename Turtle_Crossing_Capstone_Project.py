import turtle
from turtle import Turtle, Screen
import random
import time

colors=["red","yellow","blue","green","violet","orange"]
MOVE_DISTANCE = 20
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
FONT = ("Courier", 24, "normal")

game_is_on=True


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(x=20, y=-280)
        self.color("red")
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)
    
    def go_to_start(self):
        self.goto(0,-280)
    
    def at_finish_line(self):
        if self.ycor()>280:
            return True
        else:
            return False


class Car_Manager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(colors))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color="white"
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)




screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
player = Player()
car=Car_Manager()
board=Scoreboard()


screen.title("Welcome to Turtle Challenge")
screen.listen()
screen.onkey(player.go_up, "Up")




# Call update inside a loop to continuously refresh the screen

def final_score(player, car, board):
    if player.at_finish_line():
        player.go_to_start()
        car.level_up()
        board.increase_level()

while game_is_on:
   time.sleep(0.1)
   screen.update()
   car.create_car()
   car.move_car()
   for cars in car.all_cars:
        if cars.distance(player)<20:
            game_is_on=False
            board.game_over();
        final_score(player,car,board);

# You can replace this with screen.mainloop() 
turtle.done()
