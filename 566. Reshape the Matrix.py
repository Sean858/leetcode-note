#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/18 下午8:30 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 566. Reshape the Matrix.py 
# @Software: PyCharm
# ---------------------


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not nums or not len(nums):
            return nums
        m = len(nums)
        n = len(nums[0])
        if m * n != r * c:
            return nums
        res = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                index = i * c + j
                res[i][j] = nums[index // n][index % n]
        return res
