#!/usr/bin/env python
# Traditional Message Parsing

import email

banner = '-' * 48
popular_headers = ('From', 'To', 'Subject', 'Date')
msg = email.message_from_file(open('message.txt'))
headers = sorted(msg.keys())

print banner

for header in headers:
    if header not in popular_headers:
        print header + ':', msg[header]
print banner
for header in headers:
    if header in popular_headers:
        print header + ':', msg[header]
print banner
if msg.is_multipart():
    print "This program cannot handle MIME multipart messages."
else:
    print msg.get_payload()
