#!/usr/bin/python

from subprocess import call
import sys

source = "/home/simon/vocabulary/"
target = "/media/simon/Toshiba/vocabulary"
rsync = "rsync"
arguments = "-a"
cmd = "%s %s %s %s" % (rsync, arguments, source, target)

def sync():
    ret = call(cmd, shell=True)
    if ret != 0:
        print "rsync failed!"
        sys.exit(1)

sync()
