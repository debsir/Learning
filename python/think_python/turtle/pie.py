#!/usr/bin/python

import math
from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print bob

def triangle(t, apex_angle, side):
    """Draw a isosceles triangle."""
    base_angle = (180 - apex_angle) / 2
    base = int(2 * side * math.sin(math.radians(apex_angle / 2.0)))
    fd(t, side)
    lt(t, 180-apex_angle)
    fd(t, side)
    lt(t, 180-base_angle)
    fd(t, base)
    lt(t, 180)
    fd(t, base)
    rt(t, 180-base_angle)
    
def pie(t, edges, r): 
    apex_angle = 360.0 / edges
    for i in range(edges):
        triangle(t, apex_angle, r)
    wait_for_user()

pie(bob, edges=10, r=70)



