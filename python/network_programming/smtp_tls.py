#!/usr/bin/env python

import sys, smtplib, socket

if len(sys.argv) < 4:
    print "usage: %s server fromaddr toaddr [to addr...]" % sys.argv[0]
    sys.exit(2)

server, fromaddr, toaddrs = sys.argv[1], sys.argv[2], sys.argv[3:]

message = """To: %s
From: %s
Subject: Test Message from smtp_debug.py

Hello,
This is a test message sent to you from the smtp_debug.py program
in Foundations of Python Network Programming.
""" % (', '.join(toaddrs), fromaddr)

try:
    s = smtplib.SMTP(server)
    code = s.ehlo()[0]
    user_esmtp = (200 <= code <= 299)
    if not user_esmtp:
        code = s.helo()[0]
        if not (200 <= code <= 299):
            print "Remote server refused HELO; code:", code
            sys.exit(1)

    if user_esmtp and s.has_extn('starttls'):
        print "Negotiating TLS..."
        s.starttls()
        code = s.ehlo()[0]
        if not (200 <= code <= 299):
            print "Couldn't EHLO after STARTTLS"
            sys.exit(5)
        print "Using TLS connection."
    else:
        print "Server does not support TLS; using normal connection."

    s.sendmail(fromaddr, toaddrs, message)

except (socket.gaierror, socket.error, socket.herror,
        smtplib.SMTPException), e:
    print " *** Your message may not been sent!"
    print e
    sys.exit(1)
else:
    print "Message successfully sent to %d recipient(s)" % len(toaddrs)
