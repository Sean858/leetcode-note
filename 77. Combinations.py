#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/6 下午8:43 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 77. Combinations.py 
# @Software: PyCharm
# ---------------------


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        resList = []
        self.help(resList, [], n, k, 1)
        return resList

    def help(self, resList, tempList, n, k, start):
        if len(tempList) == k:
            resList.append(tempList[:])
        else:
            for i in range(start, n + 1):
                tempList.append(i)
                self.help(resList, tempList, n, k, i + 1)
                tempList.pop()



