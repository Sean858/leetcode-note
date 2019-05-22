#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/18 下午10:41 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 220. Contains Duplicate III.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if not nums or not len(nums) or k <= 0 or t < 0:
            return False
        buckets = {}
        Min = float('inf')
        for num in nums:
            Min = min(Min, num)
        diff = t + 1
        for i in range(len(nums)):
            bucket = (nums[i] - Min) // diff
            if (bucket - 1) in buckets:
                if abs(nums[i] - buckets[bucket - 1]) < diff:
                    return True
            if (bucket + 1) in buckets:
                if abs(nums[i] - buckets[bucket + 1]) < diff:
                    return True
            if bucket in buckets:
                if abs(nums[i] - buckets[bucket]) < diff:
                    return True
            buckets[bucket] = nums[i]
            if i >= k:
                buckets.pop((nums[i - k] - Min) // diff)
        return False

        # if len(nums) < 2:
        #     return False
        # if k > len(nums) - 1:
        #     k = len(nums) - 1
        # for i in range(len(nums)):
        #     for j in range(i + 1, i + k + 1):
        #         if j > len(nums) - 1:
        #             break
        #         if abs(nums[i] - nums[j]) <= t:
        #             return True
        # return False