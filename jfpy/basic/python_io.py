#!/usr/bin/python
# -*- coding: utf-8 -*-

def main_io():
    #main_rawinput()
    #input_str()
    #file_open()
    #file_read()
    #file_position()
    #file_rename_delete()
    #file_mkdir()
    file_chdir()

def main_rawinput():
    str = raw_input("请输入：")
    print "输入的内容是：",str

def input_str():
    str = input("input ：")
    print "show :"

def file_open():
    fo = open("e:\\foo.txt","wb")
    fo.write("www.baidu.com\n Very nice!")
    print "file name ",fo.name
    print "is close ",fo.closed
    print "find modle ",fo.mode
    print "+ 空格 ",fo.softspace

    fo.close()

def file_read():
    fo = open("e:\\foo.txt","rb")
    str = fo.read(10)
    print "str   ",str
    fo.close()

def file_position():
    fo = open("e:\\foo.txt","r+")
    str = fo.read(10)
    print "str  ",str

    position = fo.tell()
    print "positon  ",position

    position = fo.seek(0,0)
    str = fo.read(10)
    print "str  ",str
    fo.close()

def file_rename_delete():
    import os
    os.rename("e:\\jjj.txt","e:\\jjj1.txt")
    os.remove("e:\\jjj1.txt")

def file_mkdir():
    import  os
    os.mkdir("e:\\test1")


def file_chdir():
    import os
    #os.chdir("e:\\test1")
    os.rmdir("e:\\test1\\ff")
    os.rmdir("e:\\test1")
