#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/16 下午2:54 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 240. Search a 2D Matrix II.py 
# @Software: PyCharm
# ---------------------

class Solution(object):

    # 更好的方法
    def betterSearchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not target or not matrix or matrix[0] == 0:
            return False
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not target or not matrix or matrix[0] == 0:
            return False
        row = len(matrix)
        col = len(matrix[0])
        left, right = 0, col - 1
        for i in range(row - 1, -1, -1):
            while (left <= right):
                med = left + (right - left) // 2
                if matrix[i][med] == target:
                    return True
                elif matrix[i][med] > target:
                    right = med - 1
                else:
                    left = med + 1
            if left >= col:
                return False
            if right >= 0:
                left = right
            right = col - 1
        return False

    def main(self, matrix, target):
        print self.searchMatrix(matrix, target)

if __name__ == '__main__':
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5
    Solution().main(matrix, target)