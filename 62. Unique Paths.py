#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/3 下午2:15 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 62. Unique Paths.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        #         if m == 0 or n == 0:
        #             return 0
        #         return self.helper(m, n, 0, 0)

        #     def helper(self, m, n, x, y):
        #         if x >= n or y >= m:
        #             return 0
        #         elif x == n - 1 and y == m - 1:
        #             return 1
        #         else:
        #             return self.helper(m, n, x + 1, y) + self.helper(m, n, x, y + 1)


        # memoery
        if m == 0 or n == 0:
            return 0
        memo = {}
        return self.helper(m - 1, n - 1, memo)

    def helper(self, x, y, memo):
        if x < 0 or y < 0:
            return 0
        elif x == 0 and y == 0:
            return 1
        elif (x, y) in memo:
            return memo[(x, y)]
        else:
            memo[(x, y)] = self.helper(x - 1, y, memo) + self.helper(x, y - 1, memo)
            return memo[(x, y)]


    # DP
    def dffunction(self, m, n):
        res = [[1 for i in range(m)] for j in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                res[i][j] = res[i - 1][j] + res[i][j - 1]
        return res[-1][-1]
