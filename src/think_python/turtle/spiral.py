#!/usr/bin/python

from swampy.TurtleWorld import *
from fibonacci import fibonacci

world = TurtleWorld()
bob = Turtle()
print bob

for i in range(20):
    fd(bob, fibonacci(i))
    lt(bob, 90)
