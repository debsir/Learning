#!/usr/bin/env python

import sys, smtplib

if len(sys.argv) < 4:
    print "usage: %s server fromaddr toaddr [toaddr...]" % sys.argv[0]
    sys.exit(2)

server, fromaddr, toaddrs = sys.argv[1], sys.argv[2], sys.argv[3:]

message = """To: %s
From: %s
Subject: Test Message from simple_smtp.py

Hello,

This is a text message sent to you from the smtp_simple.py program
in Foundations of Python Network Programming.
""" % (', '.join(toaddrs), fromaddr)
s = smtplib.SMTP(server)
s.sendmail(fromaddr, toaddrs, message)

print "Message successfully sent to %d recipient(s)" % len(toaddrs)
