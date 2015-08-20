#!/usr/bin/env python
# Opening an IMAP connection with IMAPClient and listing folder information.

import email, getpass, sys
from imapclient import IMAPClient

try:
    hostname, username = sys.argv[1:]
except ValueError:
    print 'usage: %s hostname username' % sys.argv[0]
    sys.exit(2)

c = IMAPClient(hostname, ssl=True)
try:
    c.login(username, getpass.getpass())
except c.Error, e:
    print 'Could not log in:', e
    sys.exit(1)
else:
    print 'Listing mailboxes:'
    data = c.list_folders()
    for flags, delimiter, foldername in data:
        print foldername
    foldername = raw_input("Input the foldername you want to choose:\n")
    c.select_folder(foldername, readonly=True)
    msgdict = c.fetch('1:*', ['BODY.PEEK[]'])
    for message_id, message in msgdict.items():
        e = email.message_from_string(message['BODY[]'])
        print message_id, e['From']
        payload = e.get_payload()
        if isinstance(payload, list):
            part_content_types = [ part.get_content_type() for part in payload ]
            print '  Parts:', ' '.join(part_content_types)
        else:
            print '  ', ' '.join(payload[:60].split()), '...'
    c.logout()
