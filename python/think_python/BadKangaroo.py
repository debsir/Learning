class Kangaroo(object):
    
    def __init__(self, contents=[]):
        self.pouch_contents = contents

    def put_in_pouch(self, item):
        self.pouch_contents.append(item)
"""
    def __str__(self):
        t = [ object.__str__(self) + ' with pouch contents:' ]
        for obj in self.pouch_contents:
            s = '    ' + str(obj)
            t.append(s)
        return '\n'.join(t)
"""

kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
print len(kanga.pouch_contents)
print len(roo.pouch_contents)

"""
for item in roo.pouch_contents:
    print item
"""

#print kanga
#print roo

# If you run this program as is, it seems to work.
# To see the problem, trying printing roo.
