#!/usr/bin/python
# -*- coding: utf-8 -*-
def output(s,l):
    if l == 0:
        return

    print (s[l-1])
    output(s,l-1)

s = raw_input('intput a string:')
l = len(s)
output(s,l)
