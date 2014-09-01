#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-08-31 10:24:54
# @Author  : Nate Archibald (miaolei51886666@126.com)

import unittest
import roman


class KnownValues(unittest.TestCase):
    knownValues = (
        (1, 'I'),
        (2, 'II'),
        (3, 'II I'),
        (4, 'IV'),
        (5, 'V'),
        (6, 'VI'),
        (7, 'VII'),
        (8, 'VIII'),
        (9, 'IX'),
        (10, 'X'),
        (50, 'L'),
        (100, 'C'),
        (500, 'D'),
        (1000, 'M'),
        (31, 'XXXI'),
        (148, 'CXLVIII'),
        (294 , 'CCXCIV'),
        (312, 'CCCXII'),
        (421, 'CDXXI'),
        (528, 'DXXVIII'),
        (621, 'DCXXI'),
        (782, 'DCCLXXXII'),
        (870, 'DCCCLXX'),
        (941, 'CMXLI'),
        (1043, 'MXLIII'),
        (1110, 'MCX'),
        (1226, 'MCCXXVI'),
        (1301, 'MCCCI'),
        (1485, 'MCDLXXXV'),
        (1509, 'MDIX'),
        (1607, 'MDCVII'),
        (1754, 'MDCCLIV'),
        (1832, 'MDCCCXXXII'),
        (1993, 'MCMXCIII'),
        (2074, 'MMLXXIV'),
        (2152, 'MMCLII'),
        (2212, 'MMCCXII'),
        (2343, 'MMCCCXLIII'),
        (2499, 'MMCDXCIX'),
        (2574, 'MMDLXXIV'),
        (2646, 'MMDCXLVI'),
        (2723, 'MMDCCXXIII'),
        (2892, 'MMDCCCXCII'),
        (2975, 'MMCMLXXV'),
        (3051, 'MMMLI') ,
        (3185, 'MMMCLXXXV'),
        (3250, 'MMMCCL'),
        (3313, 'MMMCCCXIII'),
        (3408, 'MMMCDVIII'),
        (3501, 'MMMDI'),
        (3610, 'MMMDCX'),
        (3743, 'MMMDCCXLIII'),
        (3844, 'MMMDCCCXLIV'),
        (3888, 'MMMDCCCLXXXV III'),
        (3940, 'MMMCMXL'),
        (3999, 'MMMCMXCIX'))


    def testToRomanKnownValues(self):
        for integer, numeral in self.knownValues:
            result = roman.toRoman(integer)
            self.assertEqual(numeral, result)


# 负面测试类


class ToRomanBadInput(unittest.TestCase):
    '''
    测试输入数字，转换为罗马字符的负面测试
    '''
    def testTooLarge(self):
        #assertRaises(会引发的错误类型，对应的函数，参数)
        self.assertRaises(roman.OutOfRangeError, roman.toRoman, 4000)

    def testZero(self):
        self.assertRaises(roman.OutOfRangeError, roman.toRoman, 0)

    def testNegative(self):
        self.assertRaises(roman.OutOfRangeError, roman.toRoman, -1)

    def testNonInteger(self):
        self.assertRaises(roman.NotIntegerError, roman.toRoman, 0.5)


class FromRomanBadInput(unittest.TestCase):
    '''
    测试输入罗马字符，转换为数字的负面测试
    '''
    def testTooManyRepeatedNumerals(self):
        for s in ('MMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
            self.assertRaises(roman.InvalidRomanNumeralError, roman.fromRoman, s)

    def testRepeatedPairs(self):
        for s in ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV'):
            self.assertRaises(roman.InvalidRomanNumeralError, roman.fromRoman, s)

    def testMalfformedAntecedent(self):
        for s in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV', 'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
            self.assertRaises(roman.InvalidRomanNumeralError, roman.fromRoman, s)


# 完备性测试


class SanityCheck(unittest.TestCase):
    def testSanity(self):
        for integer in xrange(1, 4000):
            numeral = roman.toRoman(integer)
            result = roman.fromRoman(numeral)
            self.assertEqual(integer, result)


# 大小写测试


class CaseCheck(unittest.TestCase):
    def testToRomanCase(self):
        for integer in xrange(1, 4000):
            numeral = roman.toRoman(integer)
            self.assertEqual(numeral, numeral.upper())


    def testFromRomanCase(self):
        for integer in xrange(1, 4000):
            numeral = roman.toRoman(integer)
            roman.fromRoman(numeral.upper())  # 防止toRoman返回小写而导致fromRoman失败
            self.assertRaises(roman.InvalidRomanNumeralError, roman.fromRoman, numeral.lower())




























