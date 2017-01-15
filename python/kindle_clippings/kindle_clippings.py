#!/usr/bin/python
import sys, re, sqlite3
from datetime import datetime

pattern = re.compile(r'(.*?)\n- High.*?(\d+\w\d+\w\d+\w.*?\d+\w\d+\w\d+\w).*?\n\n(.*?)\n==========\n')

def grab_time(raw_time):
    # Grab date and time
    dt_obj = re.compile(r'(\d+)\w(\d+)\w(\d+)\w')
    date, time = dt_obj.findall(raw_time)
    date = '-'.join(date)
    if '上午' in raw_time:
        time = ':'.join(time) + ' ' + 'AM'
    else:
        time = ':'.join(time) + ' ' + 'PM'
    date_time = datetime.strptime(date + ' ' + time, '%Y-%m-%d %I:%M:%S %p')
    return date_time.strftime('%Y-%m-%d %H:%M:%S')
            
if __name__ == '__main__':
    clip_array = []
    with open('Kindle_Clippings.txt', 'r') as f:
        clip = f.read()
    raw_data = pattern.findall(clip)
    for slice in raw_data:
        source = slice[0]
        date_time = grab_time(slice[1])
        content = slice[2]
        clip_array.append((source, date_time, content))

    conn = sqlite3.connect('kindle_clippings.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE clip 
                    (source text, data_time real UNIQUE, content text)''')
    c.executemany('INSERT OR IGNORE INTO clip VALUES (?,?,?)', clip_array)
    conn.commit()
    conn.close()

"""
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
"""
