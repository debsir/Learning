#/usr/bin/python
import sys
import time

f = None
try:
    f = open("poem.txt")
    line = f.readline()
    if len(line) == 0:
        break
    print line,
    sys.stdout.flush()
    print "Press Ctrl+C now.\n"
    time.sleep(2)
except IOError:
    print "Could not find the file poem.txt.\n"
except KeyboardInterrupt:
    print "You cancelled the reading from the file.\n"
finally:
    if f:
        f.close()
    print "Cleaning up: close the file."
