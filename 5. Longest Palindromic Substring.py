#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/4 下午9:59 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 5. Longest Palindromic Substring.py 
# @Software: PyCharm
# ---------------------


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) < 2:
            return s
        self.l, self.r, self.maxLen = 0, 0, float('-inf')
        for i in range(1, len(s)):
            self.extend(s, i, i)
            self.extend(s, i - 1, i)
        return s[self.l: self.r + 1] if self.maxLen != float('-inf') else ""

    def extend(self, s, sl, sr):
        while sl >= 0 and sr < len(s) and s[sl] == s[sr]:
            if sr - sl + 1 > self.maxLen:
                self.maxLen = sr - sl + 1
                self.l, self.r = sl, sr
            sl -= 1
            sr += 1

#         if not s:
#             return s
#         maxLen = float('-inf')
#         start, end = 0, 0
#         dp = [[False for _ in range(len(s))] for _ in range(len(s))]

#         for i in range(len(s) - 1, -1, -1):
#             for j in range(i, len(s)):
#                 if s[i] == s[j]:
#                     if j - i <= 2:
#                         dp[i][j] = True
#                     else:
#                         dp[i][j] = dp[i + 1][j - 1]
#                 else:
#                     dp[i][j] = False
#                 if dp[i][j]:
#                     if j - i + 1 > maxLen:
#                         maxLen = j - i + 1
#                         start, end = i, j
#         return s[start:end + 1] if maxLen != float('-inf') else ""
