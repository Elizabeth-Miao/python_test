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


li = ['my', 'name', 'is', 'bob']
print '='.join(li)

print 'sss'.replace('s', 'a')


class Student(object):
    def __init__(self):
        self._score = 0
        self._birth = 1900

    @property
    def score(self):  # 只读属性
        return self._score

    @score.setter
    def score(self, value):  # 把方法变成属性赋值
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def sub_score(self):
        return 100 - self._score


s = Student()























