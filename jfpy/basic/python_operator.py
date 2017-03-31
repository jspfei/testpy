#!/usr/bin/python
# -*- coding: utf-8 -*-

#算术运算符
def python_arithmetic():
    a = 21
    b = 10
    c = 0

    c = a+ b
    print c
    c= a%b
    print c
    c = a//b
    print c

#Python比较运算符
def python_compare():
    a = 21
    b = 10
    if(a<>b):
        print "a ！= b"
    else:
        print "a = b"


#Python赋值运算符
def python_assignment():
    a = 21
    b = 10
    c = 0

    c /= a
    print c
    c = 2
    c %= a
    print c

    c **=a

    print c

#Python位运算符
def python_position():
    a = 00111100
    b = 01011100

    print "a&b = "+a&b
    print "a|b = "+a|b
    print "a^b = "+a^b
    print "~a = "+~a

#Python逻辑运算符
def python_logic():
    a = 10
    b =1
    if ( a and b ):
        print "1 - 变量 a 和 b 都为 true"
    else:
        print "1 - 变量 a 和 b 有一个不为 true"

    if ( a or b ):
        print "2 - 变量 a 和 b 都为 true，或其中一个变量为 true"
    else:
        print "2 - 变量 a 和 b 都不为 true"

    # 修改变量 a 的值
    a = 0
    if ( a and b ):
        print "3 - 变量 a 和 b 都为 true"
    else:
        print "3 - 变量 a 和 b 有一个不为 true"

    if ( a or b ):
        print "4 - 变量 a 和 b 都为 true，或其中一个变量为 true"
    else:
        print "4 - 变量 a 和 b 都不为 true"

    if not( a and b ):
        print "5 - 变量 a 和 b 都为 false，或其中一个变量为 false"
    else:
        print "5 - 变量 a 和 b 都为 true"

#  Python成员运算符
def python_member():
    a = 10
    b = 20
    list = [1,2,3,4,5]

    if(a in list):
        print "a in list"
    else:
        print "a no in list"

    if(b not in list):
        print "b in list"
    else:
        print "b no in list"

    a = 2
    if(a in list):
        print "a in list"
    else:
        print "a no in list"


