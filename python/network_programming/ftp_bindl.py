#!/usr/bin/env python

import os
from ftplib import FTP

if os.path.exists('patch8.gz'):
    raise IOError('Refusing to override your patch8.gz file')

f = FTP('ftp.kernel.org')
f.login()
f.cwd('/pub/linux/kernel/v1.0')

fd = open('patch8.gz', 'wb')
f.retrbinary('RETR patch8.gz', fd.write)
fd.close()

f.quit()
