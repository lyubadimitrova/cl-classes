#!/bin/env python

import turtle as t

t.Screen()
s = 100
t.hideturtle()
points = [(s,0), (s,s), (0,s), (0,0), (s,s), (s/2.,2.*s), (0,s), (s,0)]
for p in points: t.goto(p)
t.mainloop()
