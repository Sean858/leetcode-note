#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/27 下午11:10 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 904. Fruit Into Baskets.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """

        # Need to write again soon! Remember the exchange part.

        fir = sec = cur = secNum = res = 0
        for node in tree:
            cur = cur + 1 if node in (fir, sec) else secNum + 1
            secNum = secNum + 1 if node == sec else 1
            if sec != node:
                fir, sec = sec, node
            res = max(res, cur)
        return res


