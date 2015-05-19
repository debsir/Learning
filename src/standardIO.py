#/usr/bin/python
import sys
SN = 1
while True:
    line = sys.stdin.readline()
    if line:
        print SN, ":", line
    SN += 1
