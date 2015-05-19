#/usr/bin/python
#Find out the prime number from 0 to 100.

def is_prime(num):
    if num == 2:
        return True
    elif num > 2:
        for i in range(2, num):
            if num % i == 0:
                return False 
                break
        return True
    else:
        return False
    
for i in range(0, 101):
    if is_prime(i):
        print i
