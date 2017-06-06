#!/usr/bin/python
# -*- coding: utf-8 -*-
import Queue
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
        print_time(self.name,self.counter)
        print "Exiting "+self.name

def print_time(threadName,delay):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = delay.get()
            queueLock.release()
            print "%s processing %s" %(threadName,data)
        else:
            queueLock.release()
    time.sleep(1)


threadList = ["thread-1","thread-2","thread-3"]
nameList = ["One","Two","Three","Four","Five"]
queueLock = threading.Lock()
workQueue = Queue.Queue(10)
threads = []
threadId = 1

for tName in threadList:
    thread = myThread(threadId,tName,workQueue)
    thread.start()
    threads.append(thread)
    threadId += 1


queueLock.acquire()
for work in nameList:
    workQueue.put(work)
queueLock.release()

while not workQueue.empty():
    pass

exitFlag = 1


for t in threads:
    t.join()

print "Exiting Main Thread"