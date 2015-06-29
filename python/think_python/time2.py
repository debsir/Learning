#!/usr/bin/python

import copy

class Time(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.seconds = self.time_to_int(hour, minute, second)

    def __str__(self):
        return "%.2d:%.2d:%.2d" % self.int_to_time()
    
    def time_to_int(self, hour, minute, second):
        minutes = hour * 60 + minute
        seconds = minutes * 60 + second
        return seconds

    def int_to_time(self):
        minute, second = divmod(self.seconds, 60)
        hour, minute = divmod(minute, 60)
        return (hour, minute, second)

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)

    def print_time(self):
        print str(self)
    
    def increment(self, seconds):
        result = Time()
        result.seconds = self.seconds + seconds
        return result
    
    def add_time(self, other):
        result = Time()
        result.seconds = self.seconds + other.seconds
        return result

    def is_after(self, other):
        return self.seconds > other.seconds

    def is_valid(self):
        if time.hour < 0 or time.minute < 0 or time.second < 0:
            return False
        if time.minute >= 60 or time.second >= 60:
            return False
        return True

def main():
    start = Time(9, 45, 00)
    start.print_time()

    end = start.increment(1337)
    end.print_time()
    print "Is end after start?"
    print end.is_after(start)

    print "Using __str__"
    print start, end

    start = Time(9, 45)
    duration = Time(1, 35)
    print start + duration
    print start + 1337
    print 1337 + start

    print "Example of polymorphism"
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print total

if __name__ == "__main__":
    main()
