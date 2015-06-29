#!/usr/bin/python
#Tell whether the given year is a billextile or not.

year = int(raw_input("Please input a year:\n"))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print "The year %s is billextile!" % year
else:
    print "The year %s is not billextile!" % year

