#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-08-31 11:15:49
# @Author  : Nate Archibald (miaolei51886666@126.com)


import string
print string.punctuation
print callable(getattr(string, 'join'))
# print string.join.__doc__

class Demo:
    def say(self):
        print "hello"


d1 = Demo()
mysay = getattr(d1, 'say')
mysay()
import types
import test1
print type(getattr(d1, 'say')) == types.FunctionType
print type(getattr(test1, 'info')) == types.FunctionType

















