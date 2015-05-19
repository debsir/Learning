#!/usr/bin/python

class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    number_of_sides = 3

    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False

t = Triangle(90, 30, 60)
if t.check_angles():
    print "This is a triangle.\n"
else:
    print "This is a strange thing.\n"
