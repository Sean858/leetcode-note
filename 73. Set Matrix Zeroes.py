#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/6 上午2:24 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 73. Set Matrix Zeroes.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        row = len(matrix)
        col = len(matrix[0])
        rows = []
        cols = []

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)

        for i in range(row):
            for j in range(col):
                if i in rows or j in cols:
                    matrix[i][j] = 0

        return matrix

    # Even less space, but I don't think we need it
    def setZeroes2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        row = len(matrix)
        col = len(matrix[0])
        col0 = 1
        for i in range(row):
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(row - 1, -1, -1):
            for j in range(col - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == 0:
                matrix[i][0] = 0

        return matrix