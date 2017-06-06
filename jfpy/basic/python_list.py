#!/usr/bin/python
# -*- coding: utf-8 -*-

def list_main():
    findListData()
    changeList()
    deleteList()
    listOperater()
    listIntercept()
    listFunction2()

def findListData():
    list1 = ['jjj','ffsfs','海贼王','火影']
    list2 = [1,2,3,4,5,6]

    print "list1[0]",list1[0]
    print "list2[1:5]",list2[1:5]

def changeList():
    list1 = ['jjj','ffsfs','海贼王','火影']
    print  "value available at index 2"
    print list1[2]
    list1[2] = 2001
    print "new value available at index 2"
    print list1[2]
    print list1

def deleteList():
    list1 = ['jjj','ffsfs','海贼王','火影']
    print list1
    del list1[2]
    print "delete value at index 2"
    print list1

def listOperater():
    list1 = ['jjj','ffsfs','海贼王','火影']

    print len(list1)
    print list1+[1,3,4]
    print ["H1!"]*4
    print 3 in [1,2,3]

    for x in list1:
        print x

def listIntercept():
    L = ['Google', 'Runoob', 'Taobao']
    print L[2]
    print L[-2]
    print L[1:]

def listFunction():
    L = ['Google', 'Runoob', 'Taobao']
    L2 = ['Google', 'Runoob', 'Taobao']

    print cmp(L,L2)
    print len(L)
    print min(L)

def listFunction2():
    L = ['Google', 'Runoob', 'Taobao']
    L2 = ['a', 'b', 'c']

    print L.append(L2)
    print L
    print L2.count('a')
    L2.extend({1,2,3})
    print L2
    print L2.index('a')
    L2.insert(2,'d')
    print L2
    L2.remove('b')
    print L2
    L2.reverse()
    print L2
    L2.sort()
   # print L2





