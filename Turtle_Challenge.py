import turtle
from turtle import Turtle
import random
timmy=Turtle()
colors =["brown","dark magenta","lime green","chocolate","olive drab"]
def draw_shape(num_sides):
    angle=360/num_sides
    for i in range(num_sides):
        timmy.forward(50)
        timmy.right(angle)
for shape_side_n in range(3,10):
    timmy.color(random.choice(colors))
    draw_shape(shape_side_n)

turtle.done()  # Keep the window open until you close it manually
