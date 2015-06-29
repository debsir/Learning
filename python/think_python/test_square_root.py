#!/usr/bin/python

from square_root import square_root
import math

for i in range(1, 10):
    epsilon = abs(square_root(i) - math.sqrt(i))
    print "%.1f" % i, "\t", 
    print "%-12s" % square_root(i), "\t", 
    print "%-12s" % math.sqrt(i), "\t", 
    print "%e" % epsilon
