#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/8 上午1:32 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 48. Rotate Image.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        A = matrix[::-1]
        # method 1
        matrix[:] = [[row[i] for row in A] for i in range(len(A))]
        # method 2
        matrix[:] = map(list, zip(*A))
        # method 3
        for i in range(len(A)):
            for j in range(i):
                A[i][j], A[j][i] =  A[j][i], A[i][j]
        matrix[:] = A
