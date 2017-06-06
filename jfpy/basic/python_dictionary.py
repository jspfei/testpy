#!/usr/bin/python
# -*- coding: utf-8 -*-

def dictionary_main():
    find_dic()
    update_dic()
    delete_dic()
    inter_dic()

def find_dic():
    dict = {'name':'zara','age':7,'class':1}

    print "dict['name']" ,dict['name']
    print "dict['age']",dict['age']

def update_dic():
    dict = {'name':'zara','age':7,'class':1}

    dict['age'] = 9
    dict['school']='kkss school'

    print dict

def delete_dic():
    dict = {'name':'zara','age':7,'class':1}

    del dict['class']
    print dict
    dict.clear()
    print dict

def inter_dic():
    dict = {'name':'zara','age':7,'class':1}
    dict1 = {'name':'zara','age':7,'class':1}
    dict2 = {}
    print cmp(dict,dict1)
    print len(dict)
    print str(dict)
    print type(dict)
    print dict.copy()
    print dict.fromkeys((1,2,3),2) #创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
    print dict.get("name")
    print dict.get("ff")
    print dict.has_key("age")
    print dict.items()
    print dict.keys()
    print dict.setdefault("ffs")
    print dict.update(dict2)
    print dict2
    print dict1.values()







