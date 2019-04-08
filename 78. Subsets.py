#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/8 上午1:34 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 78. Subsets.py 
# @Software: PyCharm
# ---------------------


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        resList = []
        self.help(resList, [], nums, 0)
        return resList

    def help(self, resList, tempList, nums, start):
        resList.append(tempList[:])
        for i in range(start, len(nums)):
            tempList.append(nums[i])
            self.help(resList, tempList, nums, i + 1)
            tempList.pop()