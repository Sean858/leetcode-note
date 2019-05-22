#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/2 上午12:10 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 939. Minimum Area Rectangle.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        seen = set()
        Min = float('inf')
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    rec = abs(x2 - x1) * abs(y2 - y1)
                    if rec:
                        Min = min(Min, rec)
            seen.add((x1, y1))
        return Min if Min != float('inf') else 0