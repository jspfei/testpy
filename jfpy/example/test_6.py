#!/usr/bin/python
# -*- coding: utf-8 -*-

def fib(n):
    if n == 1 or n ==2:
        return 1
    return fib(n-1)+fib(n-2)

print fib(10)


def copy(a):
    b = a[:]
    return b

b = copy([1,2,3])
print b


