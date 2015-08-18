#!/usr/bin/env python
# POP connection and authentication

import getpass, poplib, sys

if len(sys.argv) != 3:
    print 'usage: %s hostname user' % sys.argv[0]
    exit(2)

hostname, user = sys.argv[1:]
passwd = getpass.getpass()

p = poplib.POP3_SSL(hostname)
try:
    p.user(user)
    p.pass_(passwd)
except poplib.error_proto, e:
    print "Login failed:", e
else:
    status = p.stat()
    print "You have %d message totaling  %d bytes" % status
finally:
    p.quit()

