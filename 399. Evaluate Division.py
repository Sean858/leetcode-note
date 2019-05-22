#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/5 下午9:28 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 399. Evaluate Division.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        import collections
        if not equations or not values or not queries:
            return None
        pairMap = collections.defaultdict(list)

        for (k, v), val in zip(equations, values):
            pairMap[k].append([v, val])
            pairMap[v].append([k, 1 / val])

        results = []
        for query in queries:
            result = self.dfs(query[0], query[1], pairMap, set(), 1.0)
            if result:
                results.append(result)
            else:
                results.append(-1.0)
        return results

    def dfs(self, start, end, pairMap, visited, value):
        if start not in pairMap or start in visited:
            return 0
        if start == end:
            return value
        visited.add(start)
        tmp = 0
        for i in range(len(pairMap[start])):
            tmp = self.dfs(pairMap[start][i][0], end, pairMap, \
                           visited, value * pairMap[start][i][1])
            if tmp:
                break
        visited.remove(start)
        return tmp

    def calcEquationUF(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        root = {}

        def find(x):
            p, v = root.setdefault(x, (x, 1.0))
            if x != p:
                r, vp = find(p)
                root[x] = (r, vp * v)
            return root[x]

        for (x, y), v in zip(equations, values):
            (px, vx), (py, vy) = find(x), find(y)
            if px != py: root[px] = (py, vy * v / vx)

        def q(x, y):
            if not (x in root and y in root): return -1.0
            (px, vx), (py, vy) = find(x), find(y)
            return vx / vy if px == py else -1.0

        return [q(x, y) for x, y in queries]

print(Solution().calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))









