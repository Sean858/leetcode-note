#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/1 下午12:33 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 54. Spiral Matrix.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def spiralOrder1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return res
        rowBegin, rowEnd = 0, len(matrix) - 1
        colBegin, colEnd = 0, len(matrix[0]) - 1
        while rowBegin <= rowEnd and colBegin <= colEnd:

            for i in range(colBegin, colEnd + 1):
                res.append(matrix[rowBegin][i])
            rowBegin += 1

            for i in range(rowBegin, rowEnd + 1):
                res.append(matrix[i][colEnd])
            colEnd -= 1

            if rowBegin <= rowEnd:
                for i in range(colEnd, colBegin - 1, -1):
                    res.append(matrix[rowEnd][i])
            rowEnd -= 1

            if colBegin <= colEnd:
                for i in range(rowEnd, rowBegin - 1, -1):
                    res.append(matrix[i][colBegin])
            colBegin += 1

        return res

    def spiralOrder2(self, matrix):
        return matrix and list(matrix.pop(0)) + self.spiralOrder2(zip(*matrix)[::-1])


    def main(self, matrix):
        print self.spiralOrder1(matrix)
        print self.spiralOrder2(matrix)

if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().main(matrix)