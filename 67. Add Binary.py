#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/4 下午10:56 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 67. Add Binary.py 
# @Software: PyCharm
# ---------------------


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        SUM, plus = 0, 0
        res = []
        if len(a) > len(b):
            a, b = b, a
        for i in range(len(a)):
            SUM = int(a[len(a) - 1 - i]) + int(b[len(b) - 1 - i]) + plus
            plus = SUM / 2
            SUM = 1 if SUM % 2 != 0 else 0
            res.append(SUM)
        for i in range(len(a), len(b)):
            SUM = int(b[len(b) - 1 - i]) + plus
            plus = SUM / 2
            SUM = 1 if SUM % 2 != 0 else 0
            res.append(SUM)
        if plus == 1:
            res.append(plus)

        return "".join(str(x) for x in res[::-1])