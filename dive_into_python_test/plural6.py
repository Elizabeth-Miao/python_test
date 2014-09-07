#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-08-31 10:24:54
# @Author  : Nate Archibald (miaolei51886666@126.com)


import re


def rules(language):
    for line in file('rules.%s' % language):
        pattern, search, replace = line.split()
        yield lambda word: re.search(pattern, word) and re.sub(search, replace, word)


def make_counter(x):
    print 'entering make_counter'
    while 1:
        yield x
        print 'incrementing %d' % x
        x = x + 1


counter = make_counter(2)
counter.next()
counter.next()
counter.next()


def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        print a
        a, b = b, a + b

for n in fib(1000):
    print n,