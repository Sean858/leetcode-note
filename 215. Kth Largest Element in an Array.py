#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/14 上午1:06 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 215. Kth Largest Element in an Array.py 
# @Software: PyCharm
# ---------------------


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or k < 1 or k > len(nums):
            return 0
        return self.quickSelect(nums, 0, len(nums) - 1, k)

    def quickSelect(self, nums, start, end, k):
        if start == end:
            return nums[start]
        left, right = start, end
        pivot = nums[left + (right - left) // 2]

        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if start + k - 1 <= right:
            return self.quickSelect(nums, start, right, k)
        if start + k - 1 >= left:
            return self.quickSelect(nums, left, end, k - (left - start))

        return nums[right + 1]

