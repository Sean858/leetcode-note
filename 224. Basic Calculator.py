#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/21 下午9:17 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 224. Basic Calculator.py 
# @Software: PyCharm
# ---------------------


## Easy to understand

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res, num, skip, sign = 0, 0, 0, 1
        for i in range(len(s)):
            if skip != 0:
                skip -= 1
                continue
            if s[i].isdigit():
                num = int(s[i])
                while i + 1 < len(s) and s[i + 1].isdigit():
                    num = num * 10 + int(s[i + 1])
                    i += 1
                    skip += 1
                res += num * sign
            elif s[i] in ['+', '-']:
                sign = 1 if s[i] == '+' else -1
            elif s[i] == '(':
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif s[i] == ')':
                res *= stack.pop()
                res += stack.pop()
        return res

## More concise one
class Solution1(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res, num, sign = 0, 0, 1
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in ['+', '-'] :
                res += sign * num
                num = 0
                sign = 1 if c == '+' else -1
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                res += sign * num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + sign * num