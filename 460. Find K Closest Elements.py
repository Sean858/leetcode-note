#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/5 上午1:26 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 460. Find K Closest Elements.py 
# @Software: PyCharm
# ---------------------

# 460. Find K Closest Elements
# 中文English
# Given target, a non-negative integer k and an integer array A sorted in ascending order, find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. Otherwise, sorted in ascending order by number if the difference is same.
#
# Example
# Example 1:
#
# Input: A = [1, 2, 3], target = 2, k = 3
# Output: [2, 1, 3]
# Example 2:
#
# Input: A = [1, 4, 6, 8], target = 3, k = 3
# Output: [4, 1, 6]
# Challenge
# O(logn + k) time
#
# Notice
# The value k is a non-negative integer and will always be smaller than the length of the sorted array.
# Length of the given array is positive and will not exceed 10^410 ​​
# Absolute value of elements in the array will not exceed 10^410


class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """

    def kClosestNumbers(self, A, target, k):
        # write your code here
        if not target or not k or not target:
            return []

        left, right = 0, len(A) - 1
        start = -1
        while left + 1 < right:
            med = (left + right) // 2
            if A[med] > target:
                right = med
            elif A[med] < target:
                left = med
            else:
                start = med
                break
        if start == -1:
            start = left if target - A[left] <= A[left + 1] - target else left + 1
        return self.findKClosest(A, start, target, k)

    def findKClosest(self, A, start, target, k):
        res = []
        res.append(A[start])
        l, r = start - 1, start + 1
        for _ in range(k - 1):
            if l < 0:
                res.append(A[r])
                r += 1
            elif r >= len(A):
                res.append(A[l])
                l -= 1
            elif target - A[l] <= A[r] - target:
                res.append(A[l])
                l -= 1
            else:
                res.append(A[r])
                r += 1
        return res
