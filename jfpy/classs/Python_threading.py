#!/usr/bin/python
# -*- coding: utf-8 -*-
import threading

import time

exitFlag = 0
class myThread(threading.Thread):
    def __init__(self,threadId,name,counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter

    def run(self):
        print "Starting "+self.name
        # 获得锁，成功获得锁定后返回True
        # 可选的timeout参数不填时将一直阻塞直到获得锁定
        # 否则超时后将返回False
        threadLock.acquire()
        print_time(self.name,self.counter,5)
        # 释放锁
        threadLock.release()
        print "Exiting "+self.name

def print_time(threadName,delay,counter):
    while counter:
        if exitFlag:
            threading.Thread.exit()
        time.sleep(delay)
        print "%s %s" %(threadName,time.ctime(time.time()))
        counter -= 1

threadLock = threading.Lock()
threads = []

thread1 = myThread(1,"thread-1",1)
thread2 = myThread(2,"thread-2",2)


thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()

print "Exiting Main Thread"