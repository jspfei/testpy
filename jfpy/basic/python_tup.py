#!/usr/bin/python
# -*- coding: utf-8 -*-

def main_tup():
    find_tup()
    update_tup()
    del_tup()
    operator_tup()
    findAndget_tup()
    inter_tup()

def find_tup():
    tup1 = ('y','s',1221,333)
    tup2 = (1,2,3,4,5,6)

    print "tup1[0]",tup1[0]
    print "tup2[1:5]",tup2[1:5]

def update_tup():
    tup1 = (12,34,44.3)
    tup2 = ('abc','xyz')

    tup3 = tup1 + tup2
    print tup3

def del_tup():
    print "元祖不允许删除"

def operator_tup():
    print len((1,2,3))
    print (1,3,4)+(4,5,6)
    print ("hh1")*5
    print 3 in (1,3,4)
    for x in (12,4,5):
        print x

def findAndget_tup():
    L = ('sss','ssfff','ssfffeee')
    print L[2]
    print L[-3]
    print L[1:]

def inter_tup():
    a = ('2','4','5')
    b = ('s','5','9')

    print cmp(a,b)
    print len(a)
    print max(b)
    print min(b)

