#!/usr/bin/env python
# -*- coding: utf-8 -*-


import threading
import Queue
import random


writelock = threading.Lock()


class Producer(threading.Thread):
    def __init__(self, q, con, name):
        super(Producer, self).__init__()
        self.q = q
        self.name = name
        self.con = con
        print "Producer " + self.name + " Started"

    def run(self):
        while 1:
            global writelock
            self.con.acquire()
            if self.q.full():  # 如果队列满了
                with writelock:
                    print 'Queue is full, producer wait!'
                self.con.wait()
            else:
                value = random.randint(0, 10)
                with writelock:
                    print self.name + " put value" + self.name + ":" + str(value) + " into queue."
                self.q.put((self.name + ":" + str(value)))
                self.con.notify()
            self.con.release()


class Consumer(threading.Thread):
    def __init__(self, q, con, name):
        super(Consumer, self).__init__()
        self.q = q
        self.name = name
        self.con = con
        print "Consumer " + self.name + " started\n "

    def run(self):
        while 1:
            global writelock
            self.con.acquire()
            if self.q.empty():
                with writelock:
                    print 'queue is empty, consumer wait!'
                self.con.wait()
            else:
                value = self.q.get()
                with writelock:
                    print self.name + "get value" + value + " from queue."
                self.con.notify()
            self.con.release()


if __name__ == '__main__':
    q = Queue.Queue(10)
    con = threading.Condition()
    p1 = Producer(q, con, 'P1')
    p1.start()
    p2 = Producer(q, con, 'P2')
    p2.start()
    c1 = Consumer(q, con, 'C1')
    c1.start()





































