#!/usr/bin/python
# -*- coding: utf-8 -*-
def python_while():
    numbers = [12, 35, 4, 32, 6, 3]
    even = []
    odd = []
    while len(numbers) > 0:
        number = numbers.pop()
        if( number  %  2 == 0):
            even.append(number)
        else:
            odd.append(number)
    else:
        print "numbers len < 0"

    print even
    print odd

def python_for():
    for letter in 'python':
        print ""+letter

    fruits = ['banana','apple','mango']
    for fruit in fruits:
        print '水果  ', fruit

def python_for_more():
    fruits = ['banana','apple','mango']
    for index in range(len(fruits)):
        print '水果  ',fruits[index]

def python_for_demo():
    for num in range(10,20):
        for i in range(2,num):
            if num % i == 0:
                j = num/i
                print  '%d = %d * %d' %(num,i,j)
                break
        else:
            print  num , '是一个质数'


def python_while_while():
    i = 2
    while(i < 100):
        j = 2
        while(j <= (i/j)):
            if not(i%j):break
            j = j+1
        if(j > i/j):print i,"是素数"
        i = i+1

