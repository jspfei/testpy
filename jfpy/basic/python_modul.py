#!/usr/bin/python
# -*- coding: utf-8 -*-
import python_tup
Money = 2000

def main_module():
    print Money
    addGlobalValue()
    print Money


    dirshow()



def addGlobalValue():
    global Money
    Money = Money +1

def dirshow():
    content = dir(python_tup)
    print content
