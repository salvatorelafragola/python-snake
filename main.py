from turtle import Screen
from snake import Snake
from food import Food
from poison import Poison
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)

difficult_level = screen.textinput(title="DIFFICULT", prompt="Choice a difficult level: (easy/normal)").lower()
if difficult_level == "easy" or difficult_level == "normal":


    snake = Snake()
    food = Food()
    score = Score()

    if difficult_level == "normal":
        poison = Poison()

    screen.listen()
    # Essential movements
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # If snake eat food
        if snake.head.distance(food) < 15:
            food.refresh()
            score.increase()
            snake.extend()
            if difficult_level == "normal":
                poison.refresh()

        # Snake eat poison, decraise score
        if difficult_level == "normal":
            if snake.head.distance(poison) < 15:
                snake.remove_segment()
                poison.refresh()
                score.decrease()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            score.game_over()

        # Yoi lose lifes, you're out.
        if len(snake.segments) < 1 or score.score < 0:
            game_is_on = False
            score.game_over()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                score.game_over()

else:
    print("Choice not valid")
screen.exitonclick()