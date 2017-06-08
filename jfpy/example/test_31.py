#!/usr/bin/python
# -*- coding: utf-8 -*-
weeklist = {'M':'Monday','T':{'u':'Tuesday','h':'Thursday'},'W':'Wednesday',

            'F':'Friday','S':{'a':'Saturday','u':'Sunday'}}

sLetter1 = raw_input("输入首字母:\n")
sLetter11 = sLetter1.upper()

if sLetter11 not in (weeklist.keys()):
    print "输入正确首字母"
else:
    if sLetter11 in ['T','S']:
        sLetter2 = raw_input("输入2字母:\n")
        print (weeklist[sLetter11][sLetter2])

    else:
        print (weeklist[sLetter11])
