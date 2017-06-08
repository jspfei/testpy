#!/usr/bin/python
# -*- coding: utf-8 -*-

print ('INPUT :')
n = input()
x = []
i = 0
while(n != 0):
    x.append(n%10)
    i += 1
    n /=10

print ('%d '%i)
print ('')
print (x[::])