#!/usr/bin/env python
# Command-line tool for tracing a single function in a program.

import linecache, sys, time

def make_tracer(funcname):
    def mytrace(frame, event, arg):
        if frame.f_code.co_name == funcname:
            if event == 'line':
                _events.append((time.time(), frame.f_code.co_filename,
                               frame.f_lineno))
            return mytrace
    return mytrace

if __name__ == '__main__':
    _events = []
    if len(sys.argv) < 3:
        print >> sys.stderr, 'usage: my_trace.py funcname other_script.py ...'
        sys.exit(2)
    sys.settrace(make_tracer(sys.argv[1]))
    del sys.argv[0:2]
    try:
        execfile(sys.argv[0])
    finally:
        for t, filename, lineno in _events:
            s = linecache.getline(filename, lineno)
            sys.stdout.write('%9.6f  %s' % (t % 60.0, s))


