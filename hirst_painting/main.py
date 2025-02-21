# import colorgram
#
# color = colorgram.extract("image.jpg", 30)
# rgb_colors = []
# for colors in color:
#     r = colors.rgb.r
#     g = colors.rgb.g
#     b = colors.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle

colors_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]
from turtle import Turtle, Screen
from random import choice
tim  = Turtle()
tim.penup()

tim.hideturtle()
turtle.colormode(255)
tim.speed(0)
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dot = 100

for dot_count in range(1, number_of_dot+1):
    tim.dot(20,choice(colors_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)





screen = Screen()
screen.exitonclick()



