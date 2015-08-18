#!/usr/bin/env python
# POP connection and authentication

import getpass, poplib, sys

if len(sys.argv) != 3:
    print 'usage: %s hostname user' % sys.argv[0]
    exit(2)

hostname, user = sys.argv[1:]
passwd = getpass.getpass()

p = poplib.POP3_SSL(hostname)
print "Attempting APOP authentication..."
try:
    p.apop(user, passwd)
except poplib.error_proto:
    print "Attempting standard authentication..."
    try:
        p.user(user)
        p.pass_(passwd)
    except poplib.error_proto, e:
        print "Login failed:", e
        sys.exit(1)
    else:
        status = p.stat()
        print "You have %d message totaling  %d bytes" % status
finally:
    p.quit()

