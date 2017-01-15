#!/usr/bin/python3

import re

pattern = re.compile(r'(.*?)\n- Highlight.*?(\d+\w\d+\w\d+\w.*?\d+\w\d+\w\d+\w).*?\n\n(.*?)\n==========\n')

f = open('Kindle_Clippings.txt', 'r')
clip = f.read()
f.close()
result = pattern.findall(clip)
for item in result:
    print(item, end='')
