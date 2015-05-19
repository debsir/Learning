#!/usr/bin/python

def encode(text):
    """Encode a string with ROT13."""
    ciphertext = ''
    for c in text:
        if c.isupper():
            if ord(c) + 13 > 90:
                c = chr(65 + (ord(c) + 13)%90)
            else:
                c = chr(ord(c) + 13)
        else:
            if ord(c) + 13 > 122:
                c = chr(97 + (ord(c) + 13)%122)
            else:
                c = chr(ord(c) + 13)
        ciphertext += c
    return ciphertext

def decode(ciphertext):
    text = ""
    for c in ciphertext:
        if c.isupper():
            if ord(c) - 13 < 65 :
                c = chr((ord(c) - 13) + 25)
            else:
                c = chr(ord(c) - 13)
        else:
            if ord(c) + 13 < 122:
                c = chr((ord(c) - 13) + 25)
            else:
                c = chr(ord(c) - 13)
        text += c
    return text

print decode(encode("Hello"))
