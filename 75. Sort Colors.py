#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/6 下午5:50 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 75. Sort Colors.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left, point, right = 0, 0, len(nums) - 1
        while left < right and point <= right:
            if nums[point] == 0 and left < point:
                nums[left], nums[point] = nums[point], nums[left]
                left += 1
            elif nums[point] == 2 and point < right:
                nums[point], nums[right] = nums[right], nums[point]
                right -= 1
            else:
                point += 1

        return nums

