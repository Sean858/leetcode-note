#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/23 上午2:15 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 151. Reverse Words in a String.py 
# @Software: PyCharm
# ---------------------

# join, strip, split()
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.strip().split()[::-1])
        # temp = ""
        # q = collections.deque()
        # for i in range(len(s)):
        #     if s[i] == ' ':
        #         if temp:
        #             q.append(temp)
        #             temp = ""
        #     else:
        #         temp += s[i]
        # while q:
        #     temp += " " + q.pop()
        # return temp.strip()




