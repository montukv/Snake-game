# snake game made by using freegame library

from freegames import square, vector
from turtle import *
from random import randrange


box = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change the directions"
    aim.x = x
    aim.y = y

def inside(head):
    "continue of snake is inside the walls"
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one block"
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Your points : ', len(snake))
        box.x = randrange(-15, 15) * 10
        box.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
