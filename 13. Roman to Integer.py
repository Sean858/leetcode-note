#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/8 下午8:17 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 13. Roman to Integer.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5,
             "IV": 4, "I": 1}
        i, res = 0, 0
        while i < len(s):
            if i < len(s) - 1 and s[i:i + 2] in d:
                res += d[s[i:i + 2]]
                i += 2
            elif s[i] in d:
                res += d[s[i]]
                i += 1
        return res


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        roman = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res + roman[s[-1]]