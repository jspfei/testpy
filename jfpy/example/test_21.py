#!/usr/bin/python
# -*- coding: utf-8 -*-
x2 = 1

for day in range(9,0,-1):
    x1 = (x2 +1)*2
    x2 = x1
print x1

x = 1

for day in range(0,9):
    x = (x+1)*2

print x
