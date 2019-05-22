#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/19 下午10:18 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 680. Valid Palindrome II.py 
# @Software: PyCharm
# ---------------------

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                drop_left = s[l + 1: r + 1]
                drop_right = s[l: r]
                return drop_left == drop_left[::-1] or \
                       drop_right == drop_right[::-1]
            l += 1
            r -= 1
        return True
