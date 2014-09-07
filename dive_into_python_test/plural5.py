#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-08-31 10:24:54
# @Author  : Nate Archibald (miaolei51886666@126.com)


import re
import string


def build_rule((pattern, search, replace)):
    # 表达式1 and 表达式2 如果表达式1为true，则一定返回表达式2
    # re.search()返回布尔值
    return lambda word: re.search(pattern, word) and re.sub(search, replace, word)


def plural_file(noun, language='en'):
    lines = file('rules.%s' % language).readlines()
    print type(lines)
    patterns = tuple(map(string.split, lines))
    rules = map(build_rule, patterns)
    for rule in rules:
        result = rule(noun)  # rule = re.sub(search, replace, word)
        if result:
            return result


print plural_file('sex')