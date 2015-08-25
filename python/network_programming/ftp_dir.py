#!/usr/bin/env python

from ftplib import FTP

f = FTP('ftp.kernel.org')
f.login()
f.cwd('/pub/linux/')
entries = []
f.dir(entries.append)
print "%d entries:" % len(entries)
for entry in entries:
    print entry
f.quit()
