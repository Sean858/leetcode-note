#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/6 下午12:24 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 74. Search a 2D Matrix.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        # Treat it as a sorted list
        if not matrix or not matrix[0]:
            return False

        row = len(matrix)
        col = len(matrix[0])

        left, right = 0, row * col - 1

        while left <= right:
            med = left + (right - left) // 2
            medVal = matrix[med / col][med % col]

            if medVal == target:
                return True
            elif medVal < target:
                left = med + 1
            else:
                right = med - 1

        return False

        # Rabbish method
#         if not matrix or not matrix[0]:
#             return False

#         row = len(matrix)
#         col = len(matrix[0])
#         resRow = -1

#         if row == 1:
#             if matrix[row - 1][0] > target:
#                 return False
#             else:
#                 resRow = 0
#         else:
#             for i in range(row):
#                 if matrix[i][0] > target:
#                     resRow = i - 1
#                     break

#         if resRow == -1:
#             if matrix[row - 1][col - 1] >= target:
#                 resRow = row - 1
#             else:
#                 return False

#         left, right = 0, col - 1
#         while left <= right:
#             med = left + (right - left) // 2
#             if matrix[resRow][med] == target:
#                 return True
#             elif matrix[resRow][med] < target:
#                 left = med + 1
#             else:
#                 right = med - 1
#         return False


