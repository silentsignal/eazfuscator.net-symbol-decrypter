#!/usr/bin/env python

from base64 import b64decode
from contextlib import closing
from mmap import mmap, ACCESS_READ
import re

from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor
from pbkdf2 import PBKDF2

PWD = 'InsertYourPasswordHereFromComment'

IV = PBKDF2(PWD, b64decode('HIgb2FOTjM88mSlrdaQlnV7pMzCSbH+/HuL6WG0HhA8=')).read(16)
K =  PBKDF2(PWD, b64decode('p35wEAT0D3iHdHvUnTAFwgyzmcnM+fjUVhTXN2mdbws=')).read(32)

def decrypt_word(match):
    word = match.group(1)
    c = AES.new(K, mode=AES.MODE_CBC, IV=IV)
    pt = c.decrypt(b64decode(word, '_$'))
    up = pt[:-ord(pt[-1])]
    return strxor(up[:-1], up[-1] * (len(up) - 1))

def decrypt_text(text):
    unescaped = re.sub(br'\\u([0-9A-F]{4})', decode_unicode_escape, text)
    return re.sub(br'#=q([a-zA-Z0-9\$_]+={,2})', decrypt_word, unescaped)

def decode_unicode_escape(match):
    return unichr(int(match.group(1), 16)).encode('utf-8')

def decrypt_file(name):
    with open(name) as f:
        with closing(mmap(f.fileno(), 0, access=ACCESS_READ)) as encrypted:
            return decrypt_text(encrypted)

if __name__ == '__main__':
    from sys import argv
    print decrypt_file(argv[1])
