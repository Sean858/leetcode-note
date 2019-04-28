#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/27 上午2:44 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 43. Multiply Strings.py 
# @Software: PyCharm
# ---------------------


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        # use arr to store res and add

        if not num1 or not num2:
            return None
        if num1[0] == '0' or num2[0] == '0':
            return '0'
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                l, r = i + j, i + j + 1
                Sum = mul + res[r]

                res[l] += Sum / 10
                res[r] = Sum % 10
        res = res[1:] if res[0] == 0 else res

        return "".join(str(x) for x in res)
