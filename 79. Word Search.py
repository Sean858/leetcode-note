#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/8 上午1:34 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 79. Word Search.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (self.dfs(i, j, board, word, 0)):
                    return True
        return False

    def dfs(self, i, j, board, word, num):
        if num == len(word):
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]):
            return False
        if board[i][j] != word[num]:
            return False
        temp = board[i][j]
        board[i][j] = '_'
        res = self.dfs(i + 1, j, board, word, num + 1) or self.dfs(i, j + 1, board, word, num + 1) or self.dfs(i - 1, j,
                                                                                                               board,
                                                                                                               word,
                                                                                                               num + 1) or self.dfs(
            i, j - 1, board, word, num + 1)
        board[i][j] = temp
        return res
