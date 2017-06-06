#!/usr/bin/python
# -*- coding: utf-8 -*-
def main_fun():
    show_first("调用用户自定义函数")
    show_2()
    show_3()
    show_first( str="my string")
    printinfo( age=50, name="miki" )
    printinfo1(age = 50 ,name ="fff")
    printinfo1(name='miki')
    printinfo2(10)
    printinfo2(728,21,2,23)
    lambda_function()
    print_sum()

def show_first(str):
    print str
    return

''''
传不可变实例
'''
def ChangeInt(a):
    a = 10

def show_2():
    b = 2
    ChangeInt(b)
    print b

'''传可变对象实例'''

def changeme(myList):
    myList.append([1,2,3,4])
    print "函数内取值 ：",myList
    return

def show_3():
    myList = [10,20,30]
    changeme(myList)
    print "函数外取值 ：",myList

'''关键字参数'''
def printinfo( name, age ):
    "打印任何传入的字符串"
    print "Name: ", name;
    print "Age ", age;
    return;

'''缺省参数'''
def printinfo1( name, age= 35 ):
    "打印任何传入的字符串"
    print "Name: ", name;
    print "Age ", age;
    return;

'''不定长参数'''
def printinfo2(var1,*vartuple):
    print "输出"
    print var1
    for var in vartuple:
        print var
    return

'''匿名函数'''
def lambda_function():
    sum = lambda arg1,arg2:arg1+arg2

    print "相加 ",sum(10,33)

'''return 语句'''
def sum(arg1,arg2):
    total = arg1 +arg2
    print "函数内：",total
    return total

def print_sum():
    total = sum(10,20)
    print total

