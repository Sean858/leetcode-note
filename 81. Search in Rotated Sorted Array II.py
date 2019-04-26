#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/26 上午2:56 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 81. Search in Rotated Sorted Array II.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums) - 1
        # Notice the condition, it is important!!!!!
        while l <= r:
            m = l + (r - l) // 2
            while l < m and nums[l] == nums[m]:
                l += 1
            if nums[m] == target:
                return True
            # Notice the condition, it is important!!!!!
            elif nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return False