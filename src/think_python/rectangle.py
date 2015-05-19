#!/usr/bin/python

import copy

class Point(object):
    """Represent a point."""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "(%.1f, %.1f)" % (self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Point):
            return self.merge_point(other)
        else:
            return self.move_point(other)

    def merge_point(self, other):
        target = Point()
        target.x = self.x + other.x
        target.y = self.y + other.y
        return target

    def move_point(self, offset):
        target = Point()
        target.x = self.x + offset[0]
        target.y = self.y + offset[1]
        return target
        

class Rectangle(object):
    """Represent a rectangle.
    attribute: width, height, corner
    """
    pass

def print_point(point):
    print "(%g, %g)" % (point.x, point.y)


def print_rectangle(rectangle):
    print "Corner:(%g, %g)" % (rectangle.corner.x, rectangle.corner.y) 
    print "Width:%g \nHeight:%g" % (rectangle.width, rectangle.height)

def grow_rectangle(rectangle, dwidth, dheight):
    rectangle.width += dwidth
    rectangle.height += dheight

def move_rectangle(rectangle, dx, dy):
    rectangle.corner.x += dx
    rectangle.corner.y += dy


def move_rectangle2(rectangle, dx, dy):
    rectangle2 = copy.deepcopy(rectangle)
    rectangle2.corner.x += dx
    rectangle2.corner.y += dy
    return rectangle2

p1 = Point(3, 4)
print p1.__dict__
vector = Point(-2, -3)
print p1 + vector
