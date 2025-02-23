import random
import turtle
from turtle import Turtle, Screen
from random import choice


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the race? Enter a color: ")
color = ["red","blue","yellow","orange","green","purple"]
is_race_on = False
all_turtle = []

y = 90
i = 0
def drawing_turtle():
    tim = Turtle(shape="turtle")
    tim.penup()
    global y, i
    tim.color(color[i])
    i += 1
    tim.goto(x=-240, y = y)
    y -= 30
    all_turtle.append(tim)

for _ in range(6):
    drawing_turtle()

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            wining_color = turtle.pencolor()
            is_race_on = False
            if wining_color == user_bet:
                print(f"You've won! The {wining_color} turtle is the winner")
            else:
                print(f"You've won! The {wining_color} turtle is the winner")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)




screen.exitonclick()