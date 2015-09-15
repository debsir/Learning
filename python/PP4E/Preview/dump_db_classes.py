#!/usr/bin/env python3

import shelve
db = shelve.open('class-shelve')
print("The type of db is %s." % type(db))
for key in db:
    print(key, '=>\n  ', db[key].name, db[key].pay)

bob = db['bob']
print(bob.lastName())
print(db['tom'].lastName())
