#!/usr/bin/python

from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print bob

def koch(t, x):
    if x < 3:
        fd(t, x)
        return
    koch(t, x/3)
    lt(t, 60)
    koch(t, x/3)
    rt(t, 120)
    koch(t, x/3)
    lt(t, 60)
    koch(t, x/3)

def snowflake(t):
    for i in range(3):
        koch(t, 81)
        rt(t, 120)

bob.delay = 0.01
snowflake(bob)

