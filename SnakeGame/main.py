import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title('My Snack Game')
screen.tracer(0)

# create a snake body now

snake = Snake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < - 300 or snake.head.ycor() > 280 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            game_is_on = False
            score.game_over()















screen.exitonclick()