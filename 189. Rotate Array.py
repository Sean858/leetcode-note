#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/12 下午5:26 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 189. Rotate Array.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None
        # nums[:] = nums[(len(nums) - k % len(nums)):] + nums[:(len(nums) - k % len(nums))]

        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k % len(nums) - 1)
        self.reverse(nums, k % len(nums), len(nums) - 1)

    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1