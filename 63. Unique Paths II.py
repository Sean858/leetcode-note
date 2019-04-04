#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/3 下午4:59 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 63. Unique Paths II.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or len(obstacleGrid) == 0:
            return 0
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        memo = {}
        return self.helper(obstacleGrid, row - 1, col - 1, memo)

    def helper(self, grid, row, col, memo):
        if row < 0 or col < 0 or grid[row][col] == 1:
            return 0
        elif row == 0 and col == 0:
            return 1
        elif (row, col) in memo:
            return memo[(row, col)]
        else:
            memo[(row, col)] = self.helper(grid, row - 1, col, memo) + self.helper(grid, row, col - 1, memo)
            return memo[(row, col)]

    # Need understand!
    def dpFunction(self, obstacleGrid):
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [0] * (col + 1)
        dp[1] = 1

        for i in range(row):
            for j in range(1, col + 1):
                if obstacleGrid[i][j - 1] == 1:
                    dp[j] = 0

                else:
                    dp[j] += dp[j - 1]

        return dp[-1]