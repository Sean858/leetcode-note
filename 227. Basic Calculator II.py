#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/21 下午9:53 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 227. Basic Calculator II.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        pre = 0
        cur = 0
        res = 0
        sign = '+'
        for i in range(len(s)):
            if s[i].isdigit():
                cur = cur * 10 + int(s[i])
            if not s[i].isdigit() and s[i] != ' ' or i == len(s) - 1:
                if sign == '+':
                    res += pre
                    pre = cur
                elif sign == '-':
                    res += pre
                    pre = -cur
                elif sign == '*':
                    pre *= cur
                elif sign == '/':
                    if pre // cur < 0 and pre % cur != 0:
                        pre = pre // cur + 1
                    else:
                        pre = pre // cur
                sign = s[i]
                cur = 0
        return res + pre

    # def calculate(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     num = 0
    #     stack = []
    #     sign = '+'
    #     for i in range(len(s)):
    #         if s[i].isdigit():
    #             num = num * 10 + int(s[i])
    #         if not s[i].isdigit() and s[i] != ' ' or i == len(s) - 1:
    #             if sign == '+':
    #                 stack.append(num)
    #             elif sign == '-':
    #                 stack.append(-num)
    #             elif sign == '*':
    #                 stack.append(num * stack.pop())
    #             elif sign == '/':
    #                 tmp = stack.pop()
    #                 if tmp // num < 0 and tmp % num != 0:
    #                     stack.append(tmp // num + 1)
    #                 else:
    #                     stack.append(tmp // num)
    #             sign = s[i]
    #             num = 0
    #     return sum(stack)