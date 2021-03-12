#!/bin/env python

import turtle as t
from random import randint, random, choice

# l: int (length)
# dl: int (length of line segment)
# colours: list (colour tuple)
def draw_arc(l, dl, turn='l', colours=[(0.,0.,0.)]):
    n = int(l/dl) # number of line segments
    turn_func = t.left if turn == 'l' else t.right
    for i in range(n):
        t.color(colours[i % len(colours)])
        t.forward(dl)
        turn_func(1)

def rcol():
    return random()/2.+0.5, random()/2.+0.5, random()/2.+0.5

if __name__ == '__main__':

    t.Screen()
    t.Screen().bgcolor("navy")
    t.speed(0)
    t.hideturtle()

    t.up()
    t.sety(-300)
    t.left(90)
    t.down()

    base = t.pos()
    
    for i in range(1):
        t.setheading(90)
        draw_arc(randint(100,300), randint(5,10), choice(['l', 'r']), [rcol()])
        draw_arc(randint(100,300), randint(2,6), choice(['l', 'r']), [rcol()])

        top = t.pos()

        for i in range(randint(10,15)):
            t.up()
            t.goto(top)
            t.setheading(randint(0,359))
            t.down()
            draw_arc(randint(20,30), randint(10,20), choice(['l', 'r']), [rcol()])

        t.up()
        t.goto(base)
        t.down()

    t.mainloop()
