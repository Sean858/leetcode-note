#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/8 下午9:43 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 121. Best Time to Buy and Sell Stock.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # Awesome thought, but not easy to think out at once
        minPrice, maxProfit = float('inf'), 0
        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)
        return maxProfit