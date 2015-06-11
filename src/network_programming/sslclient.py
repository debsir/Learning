#!/usr/bin/env python
#Using SSL to protect a socket

import os, socket, ssl, sys
from ssl import match_hostname, CertificateError

try:
    scrip_name, hostname = sys.argv
except ValueError:
    print >> sys.stderr, 'usage: sslclient.py <hostname>'
    sys.exit(2)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((hostname, 443))

ca_certs_path = os.path.join(os.path.dirname(scrip_name), 'certfiles.crt')
sslsock = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_SSLv3,
                          cert_reqs=ssl.CERT_REQUIRED, ca_certs=ca_certs_path)

try:
    match_hostname(sslsock.getpeercert(), hostname)
except CertificateError, ce:
    print 'Certificate error:', str(ce)
    sys.exit(1)

sslsock.sendall('Get / HTTP/1.0\r\n\r\n')
result = sslsock.makefile().read()
sslsock.close()
print 'The document https://%s/ is %d bytes long' % (hostname, len(result))
