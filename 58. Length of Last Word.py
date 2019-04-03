#!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time : 2019/4/2 下午12:36
# # @Author : Gaoxiang Chen
# # @Site :
# # @File : 58. Length of Last Word.py
# # @Software: PyCharm
# # ---------------------

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return 0 if len(s) == 0 else len(s.strip().split(' ')[-1])