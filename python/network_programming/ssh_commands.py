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

for command in 'echo "Hello, world!"', 'uname', 'uptime':
    stdin, stdout, stderr = client.exec_command(command)
    stdin.close()
    print repr(stdout.read())
    stdout.close()
    stderr.close()

client.close()
