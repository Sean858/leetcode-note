#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/22 上午8:22 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 438. Find All Anagrams in a String.py 
# @Software: PyCharm
# ---------------------

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if not p or len(p) > len(s):
            return res
        d = [0] * 26
        for i in range(len(p)):
            d[ord(p[i]) - ord('a')] += 1
            d[ord(s[i]) - ord('a')] -= 1
        if self.valid(d):
            res.append(0)
        for i in range(len(p), len(s)):
            d[ord(s[i]) - ord('a')] -= 1
            d[ord(s[i - len(p)]) - ord('a')] += 1
            if self.valid(d):
                res.append(i - len(p) + 1)
        return res
    def valid(self, d):
        if any(d) != 0:
            return False
        return True