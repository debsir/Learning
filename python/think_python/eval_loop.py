#!/usr/bin/python

def eval_loop():
    result = None
    while True:
        s = raw_input("Enter any string you want to work out:\n")
        if s == "done":
            return result
        result = eval(s)
        print "The result is %s." % eval(s)
            
if __name__ == "__main__":
    print eval_loop()
