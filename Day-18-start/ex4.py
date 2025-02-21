import turtle
from turtle import Turtle, Screen
from random import choice

tim = Turtle()

colours = ["light blue","dodger blue","slate gray","saddle brown","cornsilk","red", "blue"]
tim.pensize(15)
tim.speed(0)

direction = [0,90,180,270]

for _ in range(200):
    tim.color(choice(colours))
    tim.forward(30)
    tim.setheading(choice(direction))













screen = Screen()
screen.exitonclick()