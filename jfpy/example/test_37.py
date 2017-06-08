#!/usr/bin/python
# -*- coding: utf-8 -*-

if __name__ =="__main__":
    l = []
    for i in range(10):
        l.append(int(raw_input("输入一个数字：\n")))

    l.sort()

    print l