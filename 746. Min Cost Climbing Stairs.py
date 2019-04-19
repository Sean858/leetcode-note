#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/19 上午12:24 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 746. Min Cost Climbing Stairs.py 
# @Software: PyCharm
# ---------------------


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # 没有条件，创造条件
        cost.append(0)
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])
        return cost[-1]
