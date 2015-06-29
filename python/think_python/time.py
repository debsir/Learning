#!/usr/bin/python

import copy

class Time(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second)

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)

    def print_time(self):
        print str(self)

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def increment(self, seconds):
        seconds += self.time_to_int() 
        return int_to_time(seconds)
    
    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def is_valid(self):
        if time.hour < 0 or time.minute < 0 or time.second < 0:
            return False
        if time.minute >= 60 or time.second >= 60:
            return False
        return True

def print_time(time):
    print "%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second)

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def increment(time, seconds):
    """Modifier."""
    time.second += seconds
    if time.second >= 60:
        time.minute += time.second / 60
        time.second = time.second % 60
    if time.minute>= 60:
        time.hour += time.minute / 60
        time.minute = time.minute % 60

def increment2(time, seconds):
    """Pure function."""
    result = copy.copy(time)
    result.second += seconds
    if result.second >= 60:
        result.minute += result.second / 60
        result.second = result.second % 60
    if result.minute>= 60:
        result.hour += result.minute / 60
        result.minute = result.minute % 60
    return result

def increment3(time, seconds):
    return int_to_time((time_to_int(time) + seconds))

def is_after(t1, t2):
    return (t1.hour > t2.hour or
           t1.minute > t2.minute or
           t1.second > t2.minute)

def is_after2(t1, t2):
    return time_to_int(t1) > time_to_int(t2)

def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True

def add_time(t1, t2):
    if not valid_time(t1) or valid_time(t2):
        raise ValueError, "invalid Time object in add_time"
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

def add_time2(t1, t2):
    """Use assert statement to check given invariant."""
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

def mul_time(time, num):
    seconds = time_to_int(time) * num
    return int_to_time(seconds)

def race(time, distance):
    return mul_time(time, 1/distance)

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

    print "Example of polymorphism:"
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print total

if __name__ == "__main__":
    main()
