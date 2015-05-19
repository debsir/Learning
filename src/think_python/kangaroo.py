#!/usr/bin/python

class Kangaroo(object):
    def __init__(self):
        self.pouch_contents = []

    def put_in_pouch(self, content):
        self.pouch_contents.append(content)

kanga = Kangaroo()
kanga.put_in_pouch("key")
roo = Kangaroo()
print len(kanga.pouch_contents)
print len(roo.pouch_contents)
