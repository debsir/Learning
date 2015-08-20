#!/usr/bin/env python
# Using SSH like Telnet: connecting and running two commands

import paramiko, getpass, functools

class AllowAnythingPolicy(paramiko.MissingHostKeyPolicy):
    def missing_host_key(self, client, hostname, key):
        return

client = paramiko.SSHClient()
client.set_missing_host_key_policy(AllowAnythingPolicy())
client.connect('127.0.0.1', username=raw_input("Enter username:"), 
               password=getpass.getpass())

def my_callback(filename, bytes_so_far, bytes_total):
    print 'Transfer of %r is at %d/%d bytes (%.1f%%)' % (
        filename, bytes_so_far, bytes_total, 100. * bytes_so_far / bytes_total)

sftp = client.open_sftp()
sftp.chdir('/var/log')
for filename in sorted(sftp.listdir()):
    if filename.startswith('mail.'):
        callback_for_filename = functools.partial(my_callback, filename)
        sftp.get(filename, filename, callback=callback_for_filename)

client.close()
