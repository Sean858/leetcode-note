#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/7 上午11:09 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 12. Integer to Roman.py 
# @Software: PyCharm
# ---------------------


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        chars = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        res = ""

        for n, v in zip(chars, values):
            while num / v:
                res += n
                num = num - v
        return res

