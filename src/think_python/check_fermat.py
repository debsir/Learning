#!/usr/bin/python

def check_fermat(a, b, c, n):
    """Check Fermat's last theorem with given integers."""
    if (a ** n + b ** n == c ** n) and (n > 2):
        print "Fermat is wrong!!!"
    else:
        print "No, it doesn't work!"
        
def chanllenge():
    while True:
        numbers = raw_input("Enter 4 numbers(for a, b, c, n) seperated by comma:\n")
        (a, b, c, n) = numbers.split(",")
        check_fermat(int(a), int(b), int(c), int(n))

if __name__ == "__main__":
    chanllenge()
