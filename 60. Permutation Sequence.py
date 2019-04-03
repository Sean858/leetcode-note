#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/3 上午3:14 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 60. Permutation Sequence.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ''
        nums = []
        factor = [1] * n

        for i in range(1, n + 1):
            nums.append(i)

        for i in range(1, n):
            factor[i] = i * factor[i - 1]

        k -= 1

        for i in range(n, 0, -1):
            index = k / factor[i - 1]
            k = k % factor[i - 1]
            res += str(nums[index])
            nums.remove(nums[index])

        return res
