#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-08-31 10:24:54
# @Author  : Nate Archibald (miaolei51886666@126.com)


import re


rules = (
    (lambda word: re.search('[sxz]$', word),
     lambda word: re.sub('$', 'es', word)
    ),
    (lambda word: re.search('[^aeioudgkprt]h$', word),
     lambda word: re.sub('$', 'es', word)
    ),
    (lambda word: re.search('[^aeiou]y$', word),
     lambda word: re.sub('y$', 'ies', word)
    ),
    (lambda word: re.search('$', word),
     lambda word: re.sub('$', 's', word)
    )
)


def plural(noun):
    for match_rule, apply_rule in rules:
        if match_rule(noun):
            return apply_rule(noun)