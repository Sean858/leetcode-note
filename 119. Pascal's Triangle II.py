#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/8 下午9:17 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 119. Pascal's Triangle II.py 
# @Software: PyCharm
# ---------------------


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        # for i in range(1, rowIndex + 1):
        #     res = [1] + [res[j - 1] + res[j] for j in range(1, i)] + [1]

        # Great mathematics thought
        for _ in range(1, rowIndex + 1):
            res = [x + y for x, y in zip([0] + res, res + [0])]
        return res