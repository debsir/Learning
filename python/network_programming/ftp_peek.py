#!/usr/bin/env python
# Recursive downloader

import os, sys
from ftplib import FTP, error_perm

def walk_dir(f, dirpath):
    original_dir = f.pwd()
    try:
        f.cwd(dirpath)
    except error_perm:
        return
    print dirpath
    names = f.nlst()
    for name in names:
        walk_dir(f, dirpath + '/' + name)
    f.cwd(original_dir)

if len(sys.argv) != 2:
    print "usage: python %s <ftpserver>" % sys.argv[0]
    sys.exit(1)

ftpserver = sys.argv[1]

f = FTP(ftpserver)
f.login()
walk_dir(f, '/web')
f.quit()
