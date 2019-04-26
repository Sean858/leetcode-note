#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/26 上午2:09 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 80. Remove Duplicates from Sorted Array II.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for n in nums:
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1
        return i