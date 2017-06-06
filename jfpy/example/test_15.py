#!/usr/bin/python
# -*- coding: utf-8 -*-
def showscoreLvl(score):
    if score>= 90:
        grade = 'A'
    elif score >= 60:
        grade = 'B'
    else:
        grade = 'C'


    print '%d 属于 %s'%(score,grade)


if __name__== '__main__':
    score = int (raw_input("输入成绩："))
    showscoreLvl(score)
