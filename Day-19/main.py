from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def backwards():
    tim.backward(10)

def counter_clockwise():
    tim.left(180)

def clock_wise():
    tim.right(180)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun = backwards,key="s")
screen.onkey(fun = counter_clockwise,key="a")
screen.onkey(fun = clock_wise,key="d")
screen.onkey(fun = clear_drawing,key="c")

screen.exitonclick()