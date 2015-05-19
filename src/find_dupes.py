#!/usr/bin/python

from checksum import create_checksum
from diskwalk_api import diskwalk
from os.path import getsize

def findDupes(path = "/home/simon/Downloads"):
    dup = []
    record = []
    d = diskwalk(path)
    files = d.enumeratepaths()
    for file in files:
        compound_key = (getsize(file), create_checksum(file))
        if compound_key in record:
            dup.append(file)
        else:
            record.append(compound_key)
            #record[compound_key] = file
    return dup

if __name__ == "__main__":
    dupes = findDupes()
    for dup in dupes:
        print "Duplicate: %s" % dup

