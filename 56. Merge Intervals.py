#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/1 下午4:39 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 56. Merge Intervals.py
# @Software: PyCharm
# ---------------------


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        # Need to learn how to use the lambda
        intervals.sort(key=lambda i: i.start)
        merged = []
        for interval in intervals:
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)
        return merged



## For more lambda knowledge:
# [4,3,2,1] --> [16,9,4,1]
# print(list(map(lambda x: x ** 2, n)))
# or print([x ** 2 for x in n])
# print(list(filter(lambda x: x > 1, n)))
# or print([x for x in n if x > 1])

# Reduce: use result of operation as first param of next operation, return a item, not a list
# print(reduce(lambda x,y: x * y, n))
