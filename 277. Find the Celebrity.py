#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/16 下午8:01 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 277. Find the Celebrity.py 
# @Software: PyCharm
# ---------------------

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        character = 0
        for i in range(n):
            if knows(character, i):
                character = i
        if any(knows(character, i) for i in range(character)):
            return -1
        if any(not knows(i, character) for i in range(n)):
            return -1
        return character

        # if not n:
        #     return -1
        # row = [0] * n
        # col = [0] * n
        # for i in range(n):
        #     for j in range(n):
        #         if knows(i, j):
        #             col[j] += 1
        #             row[i] += 1
        # for i in range(n):
        #     if row[i] == 1 and col[i] == n:
        #         return i
        # return -1
