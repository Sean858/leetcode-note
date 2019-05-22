#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/7 下午9:53 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 34. Find First and Last Position of Element in Sorted Array.py 
# @Software: PyCharm
# ---------------------

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        # Find First
        start, end = -1, -1
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        if nums[r] == target:
            start = r
        if nums[l] == target:
            start = l
        if start == -1:
            return [-1, -1]

        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1
        if nums[l] == target:
            end = l
        if nums[r] == target:
            end = r
        if end == -1:
            return [-1, -1]

        return [start, end]



