#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/29 上午11:02 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 50. Pow(x, n).py 
# @Software: PyCharm
# ---------------------


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0
        if (n < 0):
            x = 1 / x
            n = -n
        ans = 1
        cur_product = x
        while n > 0:
            if n % 2 == 1:
                ans *= cur_product
            cur_product *= cur_product
            n = n / 2
        return ans
