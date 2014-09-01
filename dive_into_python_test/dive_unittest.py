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
        (148, 'CXLVII I'),
        (294 , 'CCXCIV'),
        (312, 'CCCXII'),
        (421, 'CDXXI'),
        (528, 'DXXVIII'),
        (621, 'DCXXI'),
        (782, 'DCCLXXXI I'),
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