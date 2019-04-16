#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/16 上午2:36 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 239. Sliding Window Maximum.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ## 背诵题！
        res = []
        queue = []
        for i, v in enumerate(nums):
            if queue and queue[0] <= i - k:
                queue = queue[1:]
            while queue and nums[queue[-1]] < v:
                queue.pop()
            queue.append(i)
            if i + 1 >= k:
                res.append(nums[queue[0]])
        return res

