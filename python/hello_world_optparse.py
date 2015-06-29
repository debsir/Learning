#!/usr/bin/python
from optparse import OptionParser

def main():
    p = OptionParser()
    p.add_option("--sysadmin", "-s", default="Simon")
    options, arguments = p.parse_args()
    print options, arguments
    print type(options)
    print "Hello, %s" % options.sysadmin

if __name__ == "__main__":
    main()
