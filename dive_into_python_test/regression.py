#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-08-31 10:24:54
# @Author  : Nate Archibald (miaolei51886666@126.com)

import sys
import os
import re
import unittest


def regressionTest():
    path = os.path.abspath(os.path.dirname(sys.argv[0]))
    files = os.listdir(path)
    test = re.compile('test\.py&', re.IGNORECASE)
    files = filter(test.search, files)
    filenameToModuleName = lambda f: os.path.splitext(f)[0]
    moduleNames = map(filenameToModuleName, files)
    modules = map(__import__, moduleNames)
    load = unittest.defaultTestLoader.loadTestsFromModule
    return unittest.TestSuite(map(load, modules))




def func(n):
    return n not in [1,2,3,4,5]


def map_func(n):
    return n * 2
li = [1,2,3,4,5,6]
print filter(func, li)


li2 = [5, 'a', (2, 'b')]
print map(map_func, li2)