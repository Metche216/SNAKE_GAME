from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

score = Scoreboard()
snake = Snake()
food = Food()


screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()    
    
    #Detect Collision With Food
    if snake.head.distance(food) < 15:
        score.add_point()
        snake.extend()
        food.relocate()
    
    #Detect Wall Collision
    if snake.head.xcor() > 294 or snake.head.xcor() < -294 or snake.head.ycor() > 294 or snake.head.ycor() < -294:
        score.reset()
        snake.reset()
        
    #Detect Tail Collision
    for segment in snake.segments[1:]:    
        if snake.head.distance(segment) < 10 or snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
        
screen.exitonclick() 