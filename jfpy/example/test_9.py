#!/usr/bin/python
# -*- coding: utf-8 -*-

import  time

myId = {1:'a',2:'b'}
for key,value in dict.items(myId):
    print key,value
    time.sleep(1)


print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))