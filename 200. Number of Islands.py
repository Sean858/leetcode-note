#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/12 下午11:45 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 200. Number of Islands.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        res = 0
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return res
        row = len(grid)
        col = len(grid[0])
        res = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j, row, col)
                    res += 1
        return res

    def bfs(self, grid, i, j, row, col):
        deque = collections.deque()
        deque.append((i, j))
        grid[i][j] = '-1'
        while deque:
            x, y = deque.popleft()
            directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            for d in directions:
                xx, yy = x + d[0], y + d[1]
                if 0 <= xx < row and 0 <= yy < col and grid[xx][yy] == '1':
                    deque.append((xx, yy))
                    grid[xx][yy] = '-1'

    def numIslands1(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        res = 0
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return res
        row = len(grid)
        col = len(grid[0])
        res = 0



        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j, row, col)
                    res += 1
        return res

    def dfs(self, grid, x, y, row, col):
        if x < 0 or x >= row or y < 0 or y >= col or grid[x][y] != '1':
            return
        grid[x][y] = '-1'
        self.dfs(grid, x + 1, y, row, col)
        self.dfs(grid, x, y + 1, row, col)
        self.dfs(grid, x - 1, y, row, col)
        self.dfs(grid, x, y - 1, row, col)