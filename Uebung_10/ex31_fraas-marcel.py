# Last name(s), first name(s)
# Fraas Marcel

import math     # for sqrt
import turtle   # for drawing


# Explicit functions
def draw_demo(length):
    turtle.left(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(135)
    turtle.forward(math.sqrt(2)*length)


def draw_level0(length):
    turtle.forward(length)

def draw_level1(length):
    draw_level0(length)
    turtle.left(60)
    draw_level0(length)
    turtle.right(120)
    draw_level0(length)
    turtle.left(60)
    draw_level0(length)

def draw_level2(length):
    draw_level1(length)
    turtle.left(60)
    draw_level1(length)
    turtle.right(120)
    draw_level1(length)
    turtle.left(60)
    draw_level1(length)

# Recursive functions:
def draw_rec(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        draw_rec(length, depth-1)
        turtle.left(60)
        draw_rec(length, depth-1)
        turtle.right(120)
        draw_rec(length, depth-1)
        turtle.left(60)
        draw_rec(length, depth-1)



# Useful later on:
turtle.speed('fastest')     # draws faster


# Only call ONE of the following four functions; comment the other ones using #.
#draw_demo(300)
#draw_level0(300)
#draw_level1(300)
#draw_level2(100)
draw_rec(10, 4)
turtle.right(120)
draw_rec(10, 4)
turtle.right(120)
draw_rec(10, 4)



# Useful stuff:
turtle.hideturtle()         # hides the arrow at the end
turtle.done()               # prevents the window from closing once drawing is finished.