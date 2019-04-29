#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/28 下午2:15 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 844. Backspace String Compare.py 
# @Software: PyCharm
# ---------------------


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        # ?stack and array, it seems the same, who is it?
        stack1, stack2 = [], []
        for n in S:
            if n == '#':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(n)
        for n in T:
            if n == '#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(n)
        if len(stack1) != len(stack2):
            return False
        for i in range(len(stack1)):
            if stack1[i] != stack2[i]:
                return False
        return True

    # A better way, but need understand
    # def backspaceCompare(self, S, T):
    #     i, j = len(S) - 1, len(T) - 1
    #     backS = backT = 0
    #     while True:
    #         while i >= 0 and (backS or S[i] == '#'):
    #             backS += 1 if S[i] == '#' else -1
    #             i -= 1
    #         while j >= 0 and (backT or T[j] == '#'):
    #             backT += 1 if T[j] == '#' else -1
    #             j -= 1
    #         if not (i >= 0 and j >= 0 and S[i] == T[j]):
    #             return i == j == -1
    #         i, j = i - 1, j - 1