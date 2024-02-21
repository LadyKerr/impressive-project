import turtle
import random

def draw_branch(branch_turtle, branch_length):
    angle = random.uniform(22, 30)
    sf = random.uniform(1.1, 1.3)
    branch_turtle.pensize(branch_length / 10)
    
    if branch_length < 20:
        branch_turtle.color('green')
    else:
        branch_turtle.color('brown')
    
    if branch_length < 5:
        return
    else:
        branch_turtle.forward(branch_length)
        branch_turtle.left(angle)
        draw_branch(branch_turtle, branch_length/sf)
        branch_turtle.right(angle * 2)
        draw_branch(branch_turtle, branch_length/sf)
        branch_turtle.left(angle)
        branch_turtle.backward(branch_length)

window = turtle.Screen()
window.bgcolor('black')

my_turtle = turtle.Turtle()
my_turtle.left(90)
my_turtle.up()
my_turtle.backward(300)
my_turtle.down()
my_turtle.color('brown')

draw_branch(my_turtle, 100)

window.exitonclick()
