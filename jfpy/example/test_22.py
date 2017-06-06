
#!/usr/bin/python
# -*- coding: utf-8 -*-
m1 = ['a','b','c']
m2 = ['x','y','z']

for a in m2:
    for b in m2:
        for c in m2:
            if(a !=b )and (b!=c )and(c!= a)and (a!='x')and (c!='x')and(c!='z'):
                print 'a -- %s ,b -- %s ,c -- %s'%(a,b,c)



