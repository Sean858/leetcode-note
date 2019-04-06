#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/6 上午1:40 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 72. Edit Distance.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Still need a lot of thinking, because I don't do it by myself.
        r = len(word1)
        c = len(word2)

        if r * c == 0:
            return r + c

        dist = [[0] * (c + 1) for _ in range(r + 1)]
        for i in range(r + 1):
            dist[i][0] = i
        for j in range(c + 1):
            dist[0][j] = j

        for i in range(1, r + 1):
            for j in range(1, c + 1):
                left = dist[i][j - 1] + 1
                down = dist[i - 1][j] + 1
                leftdown = dist[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    leftdown += 1
                dist[i][j] = min(left, down, leftdown)

        return dist[r][c]
