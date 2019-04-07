#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/4/6 下午7:44
# @Author : Gaoxiang Chen
# @Site :
# @File : 76. Minimum Window Substring.py
# @Software: PyCharm
# ---------------------


# Very important, remember the thought
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        import sys
        counts = {}
        for char in t:
            counts[char] = counts.get(char, 0) + 1
        for char in s:
            if char not in counts:
                counts[char] = counts.get(char, 0)
        print(counts)

        total = len(t)
        Min = sys.maxsize
        start, j = 0, 0

        for i in range(len(s)):
            if counts[s[i]] > 0:
                total -= 1
            counts[s[i]] -= 1
            while total == 0:
                if i - j + 1 < Min:
                    Min = i - j + 1
                    start = j
                counts[s[j]] += 1
                if counts[s[j]] > 0:
                    total += 1
                j += 1
        return s[start: start + Min] if Min != sys.maxsize else ""


