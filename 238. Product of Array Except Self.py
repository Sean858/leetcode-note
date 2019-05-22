#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/16 上午12:51 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 238. Product of Array Except Self.py 
# @Software: PyCharm
# ---------------------


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count, Sum = 0, 1
        for num in nums:
            if num == 0:
                count += 1
                continue
            Sum *= num
        for i in range(len(nums)):
            if count > 1:
                nums[i] = 0
            elif count == 1:
                if nums[i] == 0:
                    nums[i] = Sum
                else:
                    nums[i] = 0
            else:
                nums[i] = Sum // nums[i]
        return nums

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = []
        p = 1
        for num in nums:
            product.append(p)
            p *= num
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            product[i] *= p
            p *= nums[i]
        return product