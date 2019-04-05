#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/4 下午11:18 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 69. Sqrt(x).py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x <= 0:
            return x
        l = 1
        while l * l <= x:
            l = l * 2
        r = l
        l = l // 2
        while l + 1 < r:
            m = (l + r) // 2
            res = m * m
            if res == x:
                return m
            elif res < x:
                l = m
            else:
                r = m
        return l

    def binarySearch(self, x):
        if x <= 0:
            return x

        l, r = 1, x

        while l <= r:
            m = l + (r - l) // 2
            if m > x // m:
                r = m - 1
            else:
                if (m + 1) <= x // (m + 1):
                    l = m + 1
                else:
                    return m

    def NewTon(self, x):
        # 牛顿法讲解 https://blog.csdn.net/sinat_35678407/article/details/82764988
        r = x
        while r * r > x:
            r = (r + x / r) / 2
        return r