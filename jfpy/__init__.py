#!/usr/bin/python
# -*- coding: utf-8 -*-
from basic.python_notes import variable,python_str,python_list, python_tuple, python_dict
from classs.Python_json import show_demjson
from classs.Test import show_test
from python_condition import python_if, python_if_more
from python_file import main_file
from python_fun import main_fun
from python_function import python_function_1
from python_io import main_io
from python_loop import python_for_demo, python_while_while
from python_modul import main_module
from python_string import showStringChar,changeString,shtringOperator,stringFormatPrint,stringTripleQuotes, \
    stringFunction
from dataurl import main
from python_list import list_main
from python_time import time_main
from python_tup import main_tup
from python_dictionary import dictionary_main


def line():
    print '--------------------'

def list():
    list_main()

def getdata():
    main()

def string():
    showStringChar()
    changeString()
    shtringOperator()
    stringFormatPrint()
    line()
    stringTripleQuotes()
    line()
    stringFunction()

def function():
    python_function_1()

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

    show_demjson()
    #basic()