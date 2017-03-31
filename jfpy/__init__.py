#!/usr/bin/python
# -*- coding: utf-8 -*-
from basic.python_notes import variable,python_str,python_list, python_tuple, python_dict
from python_condition import python_if, python_if_more
from python_loop import python_for_demo, python_while_while


def line():
    print '--------------------'

def loop():
    python_for_demo()
    line()
    python_while_while()

def condition():
    python_if()
    line()
    python_if_more()

def basic():
    variable()
    line()
    python_str()
    line()
    python_list()
    line()
    python_tuple()
    line()
    python_dict()

if __name__=="__main__":
    condition()
    loop()
    # basic()