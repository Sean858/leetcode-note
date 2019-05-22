#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/20 上午10:01 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 153. Find Minimum in Rotated Sorted Array.py 
# @Software: PyCharm
# ---------------------


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l, r = 0, len(nums) - 1
        while l <= r:
            med = (l + r) // 2
            if nums[med] > nums[-1]:
                l = med + 1
            else:
                r = med - 1
        return nums[l]