#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-08-31 10:24:54
# @Author  : Nate Archibald (miaolei51886666@126.com)


import sys
import os
import re


print 'sys.argv[0]=', sys.argv[0]
pathname = os.path.dirname(sys.argv[0])
print 'path=', pathname
print 'full path =', os.path.abspath(pathname)
test = re.compile(r'.*\.pyc$', re.IGNORECASE)
files = os.listdir(os.path.abspath(pathname))  # 返回pathname所在目录下的所有文件，返回列表对象
print type(files)
print filter(test.search, files)

mylambda = lambda f: os.path.splitext(f)[0]  # splitext()分割文件，文件名&扩展名

modulenames = map(mylambda, files)
print modulenames


