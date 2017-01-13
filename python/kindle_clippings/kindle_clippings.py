#!/usr/bin/python
# coding=utf-8
import sys, re, sqlite3
from itertools import islice
from datetime import datetime

def grab_time(line):
    # Grab date and time
    dt_obj = re.compile(r'(\d+)\w(\d+)\w(\d+)\w')
    date, time = dt_obj.findall(line)
    date = '-'.join(date)
    if '上午' in line:
        time = ':'.join(time) + ' ' + 'AM'
    else:
        time = ':'.join(time) + ' ' + 'PM'
    date_time = datetime.strptime(date + ' ' + time, '%Y-%m-%d %I:%M:%S %p')
    date_time = date_time.strftime('%Y-%m-%d %H:%M:%S')
    return date_time

if __name__ == '__main__':
    clip_array = []
    with open('Kindle_Clippings.txt', 'r') as f:
        for line in f:
            source = line.strip()
            line = next(f)
            date_time = grab_time(line)
            next(f)
            content = next(f)
            next(f)
            clip_array.append((source, date_time, content))
            
    conn = sqlite3.connect('kindle_clippings.db')
    c = conn.cursor()
    try:
        c.executemany('INSERT OR IGNORE INTO sms VALUES (?,?,?)', clip_array)
    except OperationalError:
        c.execute('''CREATE TABLE sms
                    (source text, data_time real UNIQUE, content text)''')
        c.executemany('INSERT OR IGNORE INTO sms VALUES (?,?,?)', clip_array)
    conn.commit()
    conn.close()
