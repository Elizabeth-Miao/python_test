#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-08-31 11:39:14
# @Author  : Nate Archibald (miaolei51886666@126.com)


import statsout
def output(myformat="text"):
    output_func = getattr(statsout, "output_%s" % myformat, statsout.output_text)
    return output_func()


output(myformat="log")


print '' and [] and {}
print '' or [] or {}

print 'yes' if 1 == 1 else 'no'
