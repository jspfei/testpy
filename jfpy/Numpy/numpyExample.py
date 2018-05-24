#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from numpy import pi

def ndarray():
    a = np.array([2,3,4])
    print a
    print a.dtype
    b = np.array([1.2,2.3,4.1])
    print b.dtype
# 二维的数组
    b = np.array([(1.5,2,3),(43,22,1)])
    print b

# 创建时指定类型
    c = np.array([[1,2],[3,4]],dtype=complex)
    print c

    print np.zeros((3,4))

    print np.ones((2,3,4),dtype=np.int16)

    print np.empty((2,3))

    print np.arange(10,30,5)

    print np.arange(0,2,0.3)

    print np.linspace(0,2,9)

    x = np.linspace(0,2*pi,100)
    f = np.sin(x)
    print f

def basicMu():
    a = np.array([20,30,40,50])
    b = np.arange(4)
    print b

    c =a -b
    print c

    print  b**2

    print  10 *np.sin(a)

    print a<35

def martixEx():
    # 矩阵运算
    A = np.arange(10,20)
    B = np.arange(20,30)
    print A
    print B
    print A + B
    print A * B
    print A / B
    print B / A

    A = np.array([1,1,1,1])
    B = np.array([2,2,2,2])

    print A.reshape(2,2)
    print B.reshape(2,2)
    print A * B
    print np.dot(A,B)
    print A.dot(B)
    # 常用全局函数
    B = np.arange(3)
    print B
    print np.exp(B)
    C = np.array([2.,-1.,4.])
    print np.add(B,C)

#     矩阵的索引分片遍历
    print "矩阵的索引分片遍历"
    a = np.arange(10)**3

    print a
    print a[2]
    print a[2:5]
    a[:6:2] = -1000
    print a
    print a[: : -1]

    for i in a:
        print (i**(1/3.))

    print "矩阵的遍历"
    b = np.arange(16).reshape(4,4)
    for row in b:
        print (row)

    for node in b.flat:
        print (node)

    print "矩阵的特殊运算"

    print "改变矩阵形状--reshape"

    a = np.floor(10 * np.random.random((3,4)))
    print a
    print a.ravel()
    print a

    print a.reshape(2,-1)
    print a
    a.resize(2,6)
    print a

    print "矩阵合并"
    a = np.floor(10 * np.random.random((2,2)))
    print a
    b = np.floor(10*np.random.random((2,2)))
    print b
    print np.vstack((a,b))
    print np.hstack((a,b))

