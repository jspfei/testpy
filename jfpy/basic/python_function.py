#!/usr/bin/python
# -*- coding: utf-8 -*-
import random


def python_function_1():
    print "0 到 9 随机生成一个数 ", random.choice(range(10))
    print "10 dao 200 之间 3为基数 生成一个数" , random.randrange(10, 200, 3)

    list = [1,2,3,4,5,6]
    random.shuffle(list)
    print "list  随机排序", list

    print "生成一个 实数", random.uniform(1, 10)