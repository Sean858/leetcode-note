#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/20 下午6:34 
# @Author : Gaoxiang Chen
# @Site :  
# @File : Lintcode 462. Total Occurrence of Target.py
# @Software: PyCharm
# ---------------------


# 462. Total Occurrence of Target
# 中文English
# Given a target number and an integer array sorted in ascending order. Find the total number of occurrences of target in the array.
#
# Example
# Example1:
#
# Input: [1, 3, 3, 4, 5] and target = 3,
# Output: 2.
# Example2:
#
# Input: [2, 2, 3, 4, 6] and target = 4,
# Output: 1.
# Example3:
#
# Input: [1, 2, 3, 4, 5] and target = 6,
# Output: 0.
# Challenge
# Time complexity in O(logn)

class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def totalOccurrence(self, A, target):
        # write your code here
        l, r = 0, len(A) - 1
        while l <= r:
            med = (l + r) // 2
            if A[med] < target:
                l = med + 1
            else:
                r = med - 1
        fir_pos = l
        l, r = 0, len(A) - 1
        while l <= r:
            med = (l + r) // 2
            if A[med] <= target:
                l = med + 1
            else:
                r = med - 1
        last_pos = r
        return last_pos - fir_pos + 1
