#!/usr/bin/env python

from ftplib import FTP
import sys, getpass, os.path

if len(sys.argv) != 5:
    print "usage: %s <host> <username> <localfile> <remotedir>" % (
           sys.argv[0])

host, username, localfile, remotedir = sys.argv[1:]
password = getpass.getpass(
        "Enter password for %s on %s: " % (username, host))

f = FTP(host)
f.login(username, password)
f.cwd(remotedir)

fd = open(localfile, 'rb')
f.storbinary('STOR %s' % os.path.basename(localfile), fd)
fd.close()

f.quit()
