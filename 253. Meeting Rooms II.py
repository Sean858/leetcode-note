#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/13 下午11:31 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 253. Meeting Rooms II.py 
# @Software: PyCharm
# ---------------------


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([l[0] for l in intervals])
        ends = sorted([l[1] for l in intervals])
        res, end = 0, 0
        for i in range(len(starts)):
            if starts[i] < ends[end]:
                res += 1
            else:
                end += 1
        return res

#         import queue
#         q = queue.PriorityQueue()
#         intervals.sort()

#         for interval in intervals:
#             if not q.qsize():
#                 q.put(interval[1])
#                 continue
#             temp = q.get()
#             if temp > interval[0]:
#                 q.put(temp)
#             q.put(interval[1])

#         return q.qsize()





