#!/usr/bin/env python
# Basic connection to FTP server

from ftplib import FTP

f = FTP('ftp.debian.org')
print "Welcome:", f.getwelcome()
f.login()
print "Current working director:", f.pwd()
f.quit()
