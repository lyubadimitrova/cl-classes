#!/bin/env python

import turtle as t
from random import randint

# w: tuple (lower width, upper width)
# h: int (height)
# dh: int (seperation between lines)
# colours: list (colour tuple)
# starts and ends in the centre
def draw_trapezium(w, h, dh=2, colours=[(0.,0.,0.)]):
    n = int(h/dh) # number of lines
    step = int((w[1]-w[0]) / n)
    if step == 0: widths = [w[0]] * n
    else: widths = range(*w, step)
    for iw in widths:
        t.color(colours[iw % len(colours)])
        t.forward(iw/2)
        t.left(90)
        t.forward(dh)
        t.left(90)
        t.forward(iw)
        t.right(90)
        t.forward(dh)
        t.right(90)
        t.forward(iw/2)
        

if __name__ == '__main__':

    t.Screen()
    t.speed(0)
    t.hideturtle()
    t.up()
    t.sety(-300)
    t.down()
    t.color('green')

    draw_trapezium((100,100), 25, 2, [(.5,.5,0.)])

    for w in ((w,w-100) for w in range(300,50,-50)):
        colours = [(i/100., 0.5+i/100., i/100.) for i in range(-10+int(w[0]/5))]
        draw_trapezium(w, 25, 2, colours)

    t.begin_fill()
    t.color('pink')

    for i in range(15):
        x,y = randint(-50,50), randint(-200,0)
        t.up()
        t.goto(x*abs((50-y)/100),y-50)
        t.down()
        t.dot(15)

    t.mainloop()
