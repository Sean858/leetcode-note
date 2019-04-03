#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/2 下午1:47 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 59. Spiral Matrix II.py 
# @Software: PyCharm
# ---------------------


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if not n or n < 1:
            return []
        matrix = [[None for i in range(n)] for j in range(n)]
        num = 1
        rowL, rowH = 0, n - 1
        colL, colH = 0, n - 1
        while rowL <= rowH and colL <= colH:
            for i in range(colL, colH + 1):
                matrix[rowL][i] = num
                num += 1
            rowL += 1
            for i in range(rowL, rowH + 1):
                matrix[i][colH] = num
                num += 1
            colH -= 1
            if rowL <= rowH:
                for i in range(colH, colL - 1, -1):
                    matrix[rowH][i] = num
                    num += 1
                rowH -= 1
            if colL <= colH:
                for i in range(rowH, rowL - 1, -1):
                    matrix[i][colL] = num
                    num += 1
                colL += 1
        return matrix

    # Understand and remember this one.
    def generateMatrixInsideOut(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res, l = [], n ** 2 + 1
        while l > 1:
            l, h = l - len(res), l
            ## Should notice that len([[]]) = 1!
            res = [range(l, h)] + zip(*res[::-1])
        return res
