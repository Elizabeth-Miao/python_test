#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-08-31 10:24:54
# @Author  : Nate Archibald (miaolei51886666@126.com)

import re


class RomanError(Exception):
    pass


class OutOfRangeError(RomanError):
    pass


class NotIntegerError(RomanError):
    pass


class InvalidRomanNumeralError(RomanError):
    pass


romanNumeralMap = (
    ('M', 1000),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1))


def toRoman(n):
    if not(0 < n < 4000):
        raise OutOfRangeError, "number out of range (must be 1...3999)"
    if int(n) != n:
        raise NotIntegerError, "non-integers can not be converted"
    result = ""
    for numeral, integer in romanNumeralMap:
        while n >= integer:
            result += numeral
            n -= integer
    return result


romanNumeralPattern = re.compile(r'^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')


def fromRoman(s):
    if not s:
        raise InvalidRomanNumeralError, 'Input can not be blank'
    if not romanNumeralPattern.search(s):
        raise InvalidRomanNumeralError, 'Invalid Roman numeral: %s ' % s
    result = 0
    index = 0
    for numeral, integer in romanNumeralMap:
        while s[index: index + len(numeral)] == numeral:
            print s[index: index + len(numeral)]
            result += integer
            index += len(numeral)

            print 'found ', numeral, 'of length', len(numeral), ', adding', integer
    return result


print fromRoman('MMMM')























