# import another_module
# import turtle
# from turtle import Turtle, Screen
# print(another_module.another_variable)
#
# timmy = Turtle() #creae an object Turtel() is a obj of turtle module
#
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red","green")
# timmy.forward(100)
# timmy.backward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

import prettytable

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu","Squirtle", "Charmander"])
table.add_column("Type",["Electric","Water","Fire"])

table.align = "l"
print(table)

