#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

phone = "2017-33-332"#旧金山开发时间段

num = re.sub(r'#.*$',"",phone)
print num

num = re.sub(r'\D',"",phone)
print num

def double(matched):
    value = int(matched.group('value'))
    return str(value*2)

s = 'Addf2df2f3345'

print (re.sub('(?P<value>\d+)',double,s))
