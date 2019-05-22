#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/18 下午8:01 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 9. Palindrome Number.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        res = 0
        while x > res:
            res = res * 10 + x % 10
            x /= 10
        return x == res or x == (res / 10)
