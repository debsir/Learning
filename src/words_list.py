#!/usr/bin/python
import re

re_obj = re.compile(r"[A-Za-z]+")
file_name = raw_input("Enter the full path of the txt file:\n")
infile = open(file_name, "r")
word_list = []
while True:
    line = infile.readline()
    if len(line) == 0:
        break
    line = line.lower()
    match = re_obj.findall(line)
    for word in match:
        word_list.append(word)

infile.close()
word_list.sort()
for word in word_list:
    print word

