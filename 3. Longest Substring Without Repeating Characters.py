#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/9 下午2:05 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 3. Longest Substring Without Repeating Characters.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0
        charMap = {}
        longest = 0
        j = 0

        for i in range(len(s)):
            if s[i] in charMap:
                j = max(charMap.get(s[i]) + 1, j)
            charMap[s[i]] = i
            longest = max(i - j + 1, longest)
        return longest
