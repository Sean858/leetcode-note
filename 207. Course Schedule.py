#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/19 下午10:01 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 207. Course Schedule.py 
# @Software: PyCharm
# ---------------------


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        degrees = [0] * numCourses

        for i, j in prerequisites:
            edges[j].append(i)
            degrees[i] += 1

        q = collections.deque()
        for i in range(len(degrees)):
            if degrees[i] == 0:
                q.append(i)
        count = 0
        while q:
            node = q.popleft()
            count += 1
            for c in edges[node]:
                degrees[c] -= 1
                if degrees[c] == 0:
                    q.append(c)
        return count == numCourses