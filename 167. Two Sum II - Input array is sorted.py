#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/12 上午1:41 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 167. Two Sum II - Input array is sorted.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers or len(numbers) < 2:
            return None
        l, r = 0, len(numbers) - 1
        while l < r:
            Sum = numbers[l] + numbers[r]
            if Sum == target:
                return [l + 1, r + 1]
            elif Sum < target:
                l += 1
            else:
                r -= 1
        return None