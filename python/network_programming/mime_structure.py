#!/usr/bin/env python

import sys, email

def printmsg(msg, level=0):
    prefix = "|  " * level
    prefix2 = prefix + "|"
    print prefix + "+ Message Headers:"
    for header, value in msg.items():
        print prefix2, header + ":", value
    if msg.is_multipart():
        for item in msg.get_payload():
            printmsg(item, level + 1)

msg = email.message_from_file(sys.stdin)
printmsg(msg)
