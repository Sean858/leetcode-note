#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/18 下午8:56 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 217. Contains Duplicate.py 
# @Software: PyCharm
# ---------------------


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # return len(nums) != len(set(nums))

        # if not nums:
        #     return False
        # nums.sort()
        # res = nums[0]
        # for i in range(1, len(nums)):
        #     if res ^ nums[i] == 0:
        #         return True
        #     res = nums[i]
        # return False