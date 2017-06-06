#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import calendar

def time_main():
    show()
    strf_time()
    getmonth_time()
    inter_time()
    show_calendar()

def show():
    ticks = time.time()
    print "current time : ",ticks
    localtime = time.localtime(time.time())
    print "本地时间 ：",localtime[1]

    localtime1 = time.asctime(time.localtime(time.time()))
    print "本地时间 ：",localtime1

def strf_time():
    print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    # 格式化成Sat Mar 28 22:24:24 2016形式
    print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

    # 将格式字符串转换为时间戳
    a = "Sat Mar 28 22:24:24 2016"
    print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

def getmonth_time():
    cal = calendar.month(2017,5)
    print cal

def inter_time():
    print time.clock()
    time.sleep(0)
    print "ss"
    print  time.tzname[0].decode("gbk"),time.tzname[1].decode("gbk")
    print time.timezone

def show_calendar():
    print calendar.calendar(2017)
    print calendar.firstweekday()
    print calendar.isleap(2001)
    print calendar.leapdays(1988,2034)
    print calendar.month(2017,3)
    print calendar.monthrange(2017,3)
    print calendar.prcal(2082)
    print calendar.setfirstweekday(0)
    print calendar.weekday(2017,12,4)
