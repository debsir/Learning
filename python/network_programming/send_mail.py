#!/usr/bin/env python

import sys, smtplib, socket
from getpass import getpass

server = raw_input('Please enter the smtp server:\n')
sys.stdout.write("Enter username:")
username = sys.stdin.readline().strip()
password = getpass("Enter password: ")
fromaddr = username
toaddrs = raw_input('Please enter your recipients seperated by ",":\n') 
subject = raw_input("You'd better give a mail subject:\n") or "No subject"
message = raw_input("Now, it's time to write the mail.\n")

message = """To: %s
From: %s
Subject: %s
""" % (toaddrs, fromaddr, subject) + '\n' + message

try:
    s = smtplib.SMTP(server)
    try:
        s.login(username, password)
    except smtplib.SMTPException, e:
        print "Authentication failed:", e
        sys.exit(1)
    toaddrs = toaddrs.split(',')
    s.sendmail(fromaddr, toaddrs, message)
except (socket.gaierror, socket.error, socket.herror, 
        smtplib.SMTPException), e:
    print " *** Your message may not have been sent!"
    print e
    sys.exit(1)
else:
    print "Message sent to %d recipient(s)" % len(toaddrs)
