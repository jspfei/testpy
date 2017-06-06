#!/usr/bin/python
# -*- coding: utf-8 -*-

def main_file():
   # test_except()
    try:
            mye(0)
    except "Invalid level!":
        print 1
    else:
        print 2

def test_except():
    try:
        fh = open("e:\\testfile","w")
        fh.write("test")
    except IOError:
        print "error: 没有找到"
    else:
        print "input "
        fh.close()

# 定义函数
def mye( level ):
    if level < 1:
        raise Exception("Invalid level!", level)
        # 触发异常后，后面的代码就不会再执行

