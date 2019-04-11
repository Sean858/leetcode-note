#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/10 下午8:14 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 139. Word Break.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # Actually it's like the slide window problem, we can give a example to test whether there is a solution.
        d = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                if s[i - len(word) + 1 : i + 1] == word and (i - len(word) == -1 or d[i - len(word)] == True):
                    d[i] = True
        return d[-1]