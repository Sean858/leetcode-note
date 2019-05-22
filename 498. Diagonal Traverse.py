#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/16 下午9:04 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 498. Diagonal Traverse.py 
# @Software: PyCharm
# ---------------------

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return res
        m = len(matrix)
        n = len(matrix[0])

        diag = [[] for i in range(m + n - 1)]
        for i in range(m):
            for j in range(n):
                diag[i + j].append(matrix[i][j])
        i = 0
        for l in diag:
            if i % 2 == 0:
                res.extend(l[::-1])
            else:
                res.extend(l)
            i += 1
        return res
