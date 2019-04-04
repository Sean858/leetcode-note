#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/3 下午7:27 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 64. Minimum Path Sum.py 
# @Software: PyCharm
# ---------------------


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])

        dp = [[0 for i in range(row)] for j in range(col)]
        dp[0][0] = 1

        for i in range(1, row):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(1, col):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[-1][-1]

    def minPathSumWithoutExtra(self, grid):
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if i == 0 and j != 0:
                    grid[i][j] = grid[i][j - 1]
                if i != 0 and j == 0:
                    grid[i][j] = grid[i - 1][j]
                if i != 0 and j != 0:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]
