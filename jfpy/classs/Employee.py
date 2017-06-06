#!/usr/bin/python
# -*- coding: utf-8 -*-
class Employee:
    empCount = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount +=1

    def displayCount(self):
        print "total count  %d "%Employee.empCount

    def displayEmployee(self):
        print "name  : ",self.name,", Salary :",self.salary
