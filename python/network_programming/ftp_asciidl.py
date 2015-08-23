#!/usr/bin/env python
# Downloads README from remote and writes it to disk.

import os
from ftplib import FTP

if os.path.exists('README'):
    raise IOError('Refusing to override our README file')

def writeline(data):
    fd.write(data)
    fd.write(os.linesep)
        
f = FTP('ftp.kernel.org')
f.login()
f.cwd('/pub/linux/kernel')

fd = open('README', 'w')
f.retrlines('RETR README', writeline)
fd.close()

f.quit()

