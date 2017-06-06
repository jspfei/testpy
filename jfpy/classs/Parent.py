#!/usr/bin/python
# -*- coding: utf-8 -*-
class Parent:
    parentAttr = 100
    def __init__(self):
        print "调用父类构造函数"

    def parentMethod(self):
        print "调用父类方法"

    def setAttr(self,attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "父类属性：",Parent.parentAttr

    def myMethod(self):
        print '调用父类方法'

class Child(Parent):
    def __init__(self):
        print "调用子类构造方法"

    def childMedthod(self):
        print "调用子类方法 child method"

    def myMethod(self):
        print '调用子类方法'


c = Child()
c.childMedthod()
c.parentMethod()
c.setAttr(111)
c.getAttr()
c.myMethod()
