#!/usr/bin/env python

import sys, smtplib, socket
from getpass import getpass

if len(sys.argv) < 4:
    print "usage: %s server fromaddr toaddr [toaddr...]" % sys.argv[0]
    sys.exit(2)

server, fromaddr, toaddrs = sys.argv[1], sys.argv[2], sys.argv[3:]

message = """To: %s
From: %s
Subject: Test Message from smtp_login.py

Hello,

This is a text message sent to you from the smtp_simple.py program
in Foundations of Python Network Programming.
""" % (', '.join(toaddrs), fromaddr)

sys.stdout.write("Enter username:")
username = sys.stdin.readline().strip()
password = getpass("Enter password: ")

try:
    s = smtplib.SMTP(server)
    try:
        s.login(username, password)
    except smtplib.SMTPException, e:
        print "Authentication failed:", e
        sys.exit(1)
    s.sendmail(fromaddr, toaddrs, message)
except (socket.gaierror, socket.error, socket.herror, 
        smtplib.SMTPException), e:
    print " *** Your message may not have been sent!"
    print e
    sys.exit(1)
else:
    print "Message successfully sent to %d recipient(s)" % len(toaddrs)
