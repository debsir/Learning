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

f = FTP('ftp.kernel.org')
f.login()
walk_dir(f, '/pub/linux/kernel/Historic/old-versions')
f.quit()
