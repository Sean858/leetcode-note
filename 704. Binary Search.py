#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/19 下午11:48 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 704. Binary Search.py 
# @Software: PyCharm
# ---------------------

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            med = (l + r) // 2
            if nums[med] == target:
                return med
            elif nums[med] > target:
                r = med - 1
            else:
                l = med + 1
        return -1
