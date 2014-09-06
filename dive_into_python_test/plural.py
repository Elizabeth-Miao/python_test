#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-08-31 10:24:54
# @Author  : Nate Archibald (miaolei51886666@126.com)


import re


def plural(noun):
    if re.search(r'[sxz]$', noun):
        return re.sub('$', 'es', noun)
    elif re.search(r'[^aeioudgkprt]h$', noun):  # ^符号加在[]中表示
        return re.sub('$', 'es', noun)
    elif re.search(r'[^aeiou]y$', noun):
        return re.sub('y$', 'ies', noun)
    else:
        return noun + 's'


print plural('cheetah')