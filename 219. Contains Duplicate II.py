#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/18 下午9:02 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 219. Contains Duplicate II.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                if abs(i - d[nums[i]]) <= k:
                    return True
            d[nums[i]] = i
        return False
