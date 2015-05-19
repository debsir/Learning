#!/usr/bin/python
from math import factorial
from has_duplicates import has_duplicates2
from random import randint

def nCr(n, r):
    f = factorial
    return f(n) / f(n-r) / f(r) 

def nPr(n, r):
    f = factorial
    return f(n) / f(n-r)
"""
def sampling(sample_size, population):
    birth_sample = []
    for i in range(sample_size):
        birthday = population[randint(0,365)]
        birth_sample.append(birthday)
    return birth_sample
"""

def sampling(sample_size, population):
    birth_sample = [population[randint(0,365)] for i in range(sample_size)]
    return birth_sample

month_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
day_list = [str(day) for day in range(1,32)]
birth_list = []
for month in month_list:
    for day in day_list:
        birth_list.append(month + "-" + day)

wrong_list = ["Feb-30", "Feb-31", "Apr-31", "Jun-31", "Sep-31", "Nov-31"]
birth_list = list(set(birth_list) - set(wrong_list))

count = 0
for i in range(100000):
    birth_sample = sampling(23, birth_list)
    if has_duplicates2(birth_sample):
        count += 1

print "Simulated stats prob:\n"
print count / float(100000)

print "Theoretical prob:\n"
prob = (366 ** 23 - nPr(366, 23)) / float(366 ** 23) 
print prob
