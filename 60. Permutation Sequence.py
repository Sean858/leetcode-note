#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/3 上午3:14 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 60. Permutation Sequence.py 
# @Software: PyCharm
# ---------------------

class Solution(object):

    #         k = k - 1
    #
    #         i = 3, k = 2
    #         factor[i - 1] = 2
    #         index = k / factor[i - 1] = 1 => index 1 in (1, 2, 3) => 2
    #         remove 2 from (1, 2, 3) => (1, 3)
    #         k = k % factor[i - 1] = 0

    #         i = 2, k = 0
    #         factor[i - 1] = 1
    #         index = k / factor[i - 1] = 0 => index 0 in (1, 3) => 1
    #         remove 1 from (1, 3) => (3)
    #         k = k % factor[i - 1] = 0

    #         i = 1, k = 0
    #         factor[i - 1] = 1
    #         index = k / factor[i - 1] = 0 => index 0 in (3) => 3
    #         ...

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
