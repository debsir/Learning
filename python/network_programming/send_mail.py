#!/usr/bin/env python

import sys, smtplib, socket, mimetypes
from getpass import getpass
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import utils, encoders

def genpart(data, contenttype):
    maintype, subtype = contenttype.split('/')
    if maintype == 'text':
        retval = MIMEText(data, _subtype=subtype)
    else:
        retval = MIMEBase(maintype, subtype)
        retval.set_payload(data)
        encoders.encode_base64(retval)
    return retval

def attachment(filename):
    fd = open(filename, 'rb')
    mimetype, mimeencoding = mimetypes.guess_type(filename)
    if mimeencoding or (mimetype is None):
        mimetype = 'application/octet-stream'
    retval = genpart(fd.read(), mimetype)
    retval.add_header('Content-Disposition', 'attachment',
                      filename = filename)
    fd.close()
    return retval

server = raw_input('Please enter the smtp server:\n')
sys.stdout.write("Enter username:")
username = sys.stdin.readline().strip()
password = getpass("Enter password: ")
fromaddr = username
toaddrs = raw_input('Please enter your recipients seperated by ",":\n') 
subject = raw_input("You'd better give a mail subject:\n") or "No subject"
message = raw_input("Now, it's time to write the mail.\n")
attach_file = raw_input("Type the attach file name if needed:\n") or None

msg = MIMEMultipart()
msg['To'] = toaddrs
msg['From'] = fromaddr
msg['Subject'] = subject
msg['Date'] = utils.formatdate(localtime=1)
msg['Message-ID'] = utils.make_msgid()

body = MIMEMultipart('alternative')
body.attach(genpart(message, 'text/plain'))
msg.attach(body)

if attach_file:
    msg.attach(attachment(attach_file))

mail = msg.as_string()

try:
    s = smtplib.SMTP(server)
    try:
        s.login(username, password)
    except smtplib.SMTPException, e:
        print "Authentication failed:", e
        sys.exit(1)
    toaddrs = toaddrs.split(',')
    s.sendmail(fromaddr, toaddrs, mail)
except (socket.gaierror, socket.error, socket.herror, 
        smtplib.SMTPException), e:
    print " *** Your message may not have been sent!"
    print e
    sys.exit(1)
else:
    print "Message sent to %d recipient(s)" % len(toaddrs)

