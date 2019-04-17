#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/16 下午11:56 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 242. Valid Anagram.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1 = [0] * 26
        for char in s:
            dict1[ord(char) - ord('a')] += 1
        for char in t:
            dict1[ord(char) - ord('a')] -= 1
        return not any(dict1)

        # return sorted(s) == sorted(t)