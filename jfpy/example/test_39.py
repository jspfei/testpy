#!/usr/bin/python
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    a = [1,3,4,5,6,9,12,14,15,17,0]

    num = int (raw_input("input a number:\n"))
    #a.append(num)
    #a.sort()
    #print a

    print a

    end = a[9]
    if num >end:
        a[10] = num
    else:
        for i in range(10):
            if a[i]>num:
                temp1 = a[i]
                a[i] = num
                for j in range(i+1,11):
                    temp2 = a[j]
                    a[j] = temp1
                    temp1 = temp2
                break
    print a
