#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/21 下午8:11 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 268. Missing Number.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums)
        # return n * (n + 1) // 2 - sum(nums)

        n = len(nums)
        for i in range(len(nums)):
            n ^= i ^ nums[i]
        return n