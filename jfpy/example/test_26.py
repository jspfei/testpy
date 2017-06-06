#!/usr/bin/python
# -*- coding: utf-8 -*-

def fact(n):
    sum = 0
    if n == 0 :
        sum = 1
    else:
        sum = n*fact(n-1)
    return sum

t = int(raw_input("num : "))
print fact(t)
