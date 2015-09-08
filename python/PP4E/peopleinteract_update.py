#!/usr/bin/env python3

import shelve
from person_alternative import Person

fieldnames = ('name', 'age', 'job', 'pay')
db = shelve.open('class-shelve')

while True:
    key = input('\nKey? => ')
    if not key: break
    elif key in db:
        record = db[key]
    else:
        record = Person(name='?', age='?')
    for field in fieldnames:
        currval = getattr(record, field)
        newtext = input('\t[%s]=%s\n\t\tnew?=>' % (field, currval))
        if newtext:
            setattr(record, field, eval(newtext))
    db[key] = record
db.close()
