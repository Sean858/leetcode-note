#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/19 下午5:26 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 763. Partition Labels.py 
# @Software: PyCharm
# ---------------------

## 贪心
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last = {c: i for i, c in enumerate(S)}
        res = []
        j, old = 0, 0
        for i, c in enumerate(S):
            j = max(j, last[c])
            if j == i:
                res.append(i - old + 1)
                old = i + 1
        return res










