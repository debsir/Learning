#!/usr/bin/env python3

"""
Implement an HTTP web server in Python that knows how to run server-side
CGI scripts coded in Python; serves files and scripts from current working
dir; Python scripts must be stored in webdir\cgi-bin or webdir\htbin;
"""

import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'
port = 8080

os.chdir(webdir)
srvraddr = ("", port)
srvobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvobj.serve_forever()
