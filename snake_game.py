import turtle
from random import randint
from time import sleep
main_screen = turtle.Screen()
main_screen.setup(600, 600)
main_screen.bgcolor("black")
main_screen.title("turtle")
# main_screen.register_shape("strawberry.gif")
main_screen.tracer(False)
def create_turtle(shape, color):
    my_turtle = turtle.Turtle()
    my_turtle.shape(shape)
    my_turtle.color(color)
    my_turtle.penup()
    return my_turtle

def change_position(object):
    x = randint(-270,270)
    y = randint(-270,240)
    object.goto(x,y)

def move_snake():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        y += 20
        snake_head.sety(y)

def go_up():
    snake_head.direction = "up"

def on_close():
    global running
    running = False

root = main_screen._root
root.protocol("WM_DELETE_WINDOW", on_close)

snake_head = create_turtle("square", "green")
snake_head.direction = ""
# snake_head = create_turtle("strawberry.gif", "green")
snake_food = create_turtle("circle", "red")
change_position(snake_food)

main_screen.listen()
main_screen.onkeypress(go_up, "Up")
# TODO  سایر جهت ها را نیز انجام بده
running = True
while running:
    main_screen.update()
    move_snake()
    sleep(0.2)



