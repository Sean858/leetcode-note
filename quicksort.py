#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/2 上午1:13 
# @Author : Gaoxiang Chen
# @Site :  
# @File : quicksort.py 
# @Software: PyCharm
# ---------------------


class Solution():
    def quickSort(self, A):
        self.sort(A, 0 , len(A) - 1)
        return A

    def sort(self, A, start, end):
        if start >= end:
            return 0
        left, right = start, end
        mid = A[left + (right - left) // 2]
        while left <= right:
            while left <= right and A[left] < mid:
                left += 1
            while left <= right and A[right] > mid:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]

                left += 1
                right -= 1

        self.sort(A, start, right)
        self.sort(A, left, end)

if __name__ == '__main__':
    print(Solution().quickSort([3,5,8,1,2,0,2]))

