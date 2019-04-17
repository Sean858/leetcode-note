#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/17 上午1:01 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 387. First Unique Character in a String.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = collections.Counter(s)

        index = 0
        for ch in s:
            if count[ch] == 1:
                return index
            else:
                index += 1
        return -1

#         import sys
#         dict1 = [[0, 0] for _ in range(26)]
#         first = sys.maxsize

#         for i in range(len(s)):
#             dict1[ord(s[i]) - ord('a')][0] = i
#             dict1[ord(s[i]) - ord('a')][1] += 1
#         for i in range(len(dict1)):
#             if dict1[i][1] == 1:
#                 first = min(first, dict1[i][0])
#         return first if first != sys.maxsize else -1


