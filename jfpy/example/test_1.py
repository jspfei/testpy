#!/usr/bin/python
# -*- coding: utf-8 -*-

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i != k) and (i != j) and (j != k):
                print i,j,k



from itertools import permutations

for i in permutations([1,2,3,4],3):
    print (i)