#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-08-31 10:24:54
# @Author  : Nate Archibald (miaolei51886666@126.com)


import re


def buildMatchAndApplyFunctions((pattern, search, replace)):
    matchFunction = lambda word: re.search(pattern, word)
    applyFunction = lambda word: re.sub(search, replace, word)
    return (matchFunction, applyFunction)


patterns = (
    ('[sxz]$', '$', 'es'),
    ('[^aeioudgkprt]h$', '$', 'es'),
    ('(qu[^aeiou])y$', 'y$', 'ies'),
    ('$', '$', 's')
)


rules = map(buildMatchAndApplyFunctions, patterns)
# (<function <lambda> at 0x00000000023A26D8>, <function <lambda> at 0x00000000023A2748>)
def plural(noun):
    for match_rule, apply_rule in rules:
        if match_rule(noun):
            return apply_rule(noun)


def foo((a, b, c)):
    print c
    print b
    print a

params = ['apple', 'bear', 'catnap']
foo(params)
