#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/10 上午11:39 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 973. K Closest Points to Origin.py 
# @Software: PyCharm
# ---------------------


class Solution:
    def kClosest(self, points, K):
        dist = [[x ** 2 + y ** 2, (x, y)] for x, y in points]
        return self.quickSelect(dist, K, 0, len(dist) - 1)

    def quickSelect(self, dist, K, start, end):
        if start == end:
            return [y for x, y in dist[:start + 1]]
        left, right = start, end
        piv = dist[(left + right) // 2][0]

        while left <= right:
            while left <= right and dist[left][0] < piv:
                left += 1
            while left <= right and dist[right][0] > piv:
                right -= 1
            if left <= right:
                dist[left], dist[right] = dist[right], dist[left]
                left += 1
                right -= 1

        if start + K - 1 <= right:
            return self.quickSelect(dist, K, start, right)
        if start + K - 1 >= left:
            return self.quickSelect(dist, K - (left - start), left, end)
        return [y for x, y in dist[:right + 2]]


class Solution1:
    def kClosest(self, points, K):

        dist = [x ** 2 + y ** 2 for x, y in points]

        # Queue py3, queue py2
        import queue
        q = queue.PriorityQueue()

        for i in range(len(dist)):
            q.put((-dist[i], points[i]))
            if q.qsize() > K:
                q.get()

        res = []
        while K > 0:
            res.append(q.get()[1])
            K -= 1
        return res

#   Test Case
#   [[1,3],[-2,2],[2,-2]]
#   2

