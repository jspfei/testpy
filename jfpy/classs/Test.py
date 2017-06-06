#!/usr/bin/python
# -*- coding: utf-8 -*-
from classs.Employee import Employee


class Test:
    def prt(self):
        print (self)
        print (self.__class__)


def show_test():
    '''
    t = Test()
    t.prt()
    :return:
    '''
    class_test()

def class_test():
    emp1 = Employee("zara",1000)
    emp2 = Employee("mma",2222)

    emp1.displayEmployee()
    emp2.displayEmployee()
    emp1.age = 7
    emp1.age = 8
    del emp1.age
    print "total  employee  %d"%Employee.empCount

    del emp1
    print "Employee.doc ",Employee.__doc__
    print "Employee.name ",Employee.__name__
    print "Employee.__module__ ",Employee.__module__
    print "Employee.bases ",Employee.__bases__
    print "Employee.dict ",Employee.__dict__





