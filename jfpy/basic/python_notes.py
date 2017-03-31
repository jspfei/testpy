#!/usr/bin/python
# -*- coding: utf-8 -*-

# 第一注释

def notes():
    print "Python notes"  # 第二注释

'''
变量赋值
'''


def variable():
    counter = 100  # 赋值 整型变量
    miles = 1000.0  # 浮点型
    name = 'json'  # 字符串
    print counter
    print miles
    print name


def python_str():
    str = 'hello world!'
    print str
    print str[0]
    print str[2:6]
    print str[2:]
    print str * 2
    print str + "Test"

#list 可以更新
def python_list():
    list = ['runoob',754,1.1,'json',87]
    tinylist =[123,'john']

    print list
    list[2] = 1000
    print list[0]
    print list[1:3]
    print list[2:]
    print tinylist * 2
    print list + tinylist

#元祖不允许更新
def python_tuple():
    tuple = ('ruboon',333,22.1,'json')
    tinytuple = (123,'john')

    print tuple
    print tuple[0]
    print tuple[1:3]
    print tuple[2]
    print tinytuple * 2
    print tuple + tinytuple

#字典
def python_dict():
    dict = {}
    dict['one'] = "this is one"
    dict[2] = 'this is two'
    tinydict = {'name':'json','code':3322 ,'dept':'sales'}

    print dict['one']
    print dict[2]
    print tinydict
    print tinydict.keys()
    print tinydict.values()

'''
Python数据类型转换
函数	描述
int(x [,base])
将x转换为一个整数
long(x [,base] )
将x转换为一个长整数
float(x)
将x转换到一个浮点数
complex(real [,imag])
创建一个复数
str(x)
将对象 x 转换为字符串
repr(x)
将对象 x 转换为表达式字符串
eval(str)
用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s)
将序列 s 转换为一个元组
list(s)
将序列 s 转换为一个列表
set(s)
转换为可变集合
dict(d)
创建一个字典。d 必须是一个序列 (key,value)元组。
frozenset(s)
转换为不可变集合
chr(x)
将一个整数转换为一个字符
unichr(x)
将一个整数转换为Unicode字符
ord(x)
将一个字符转换为它的整数值
hex(x)
将一个整数转换为一个十六进制字符串
oct(x)
将一个整数转换为一个八进制字符串



'''

