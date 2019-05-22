#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/7 下午9:39 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 29. Divide Two Integers.py 
# @Software: PyCharm
# ---------------------


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        mul = 1
        if dividend < 0:
            mul *= -1
            dividend = -1 * dividend
        if divisor < 0:
            mul *= -1
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            delete, ind = divisor, 1
            while dividend >= delete:
                dividend -= delete
                res += ind
                delete <<= 1
                ind <<= 1
        if mul == -1:
            res *= mul

        # A good way to make restriction
        return min(max(- 2 ** 31, res), 2 ** 31 - 1)


