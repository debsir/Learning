#!/usr/bin/env python

from email.mime.text import MIMEText
from email.header import Header

message = """Hello,

This is a test message from Chapter 12. I hope you enjoy it!

---Anonymous
"""

msg = MIMEText(message)
msg['To'] = 'recipient@example.com'
fromhdr = Header()
fromhdr.append(u"Michael M\xfcller")
fromhdr.append('<mmueller@example.com>')
msg['From'] = fromhdr
msg['Subject'] = 'Test Message, Chapter 12'

print msg.as_string()
