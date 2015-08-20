#!/usr/bin/env python
# Using SSH like Telnet: connecting and running two commands

import paramiko, getpass

class AllowAnythingPolicy(paramiko.MissingHostKeyPolicy):
    def missing_host_key(self, client, hostname, key):
        return

client = paramiko.SSHClient()
client.set_missing_host_key_policy(AllowAnythingPolicy())
client.connect('127.0.0.1', username=raw_input("Enter username:"), 
               password=getpass.getpass())

channel = client.invoke_shell()
stdin = channel.makefile('wb')
stdout = channel.makefile('rb')

stdin.write('echo Hello, world\rexit\r')
print stdout.read()

client.close()
