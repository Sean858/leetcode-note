#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/17 上午1:00 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 150. Evaluate Reverse Polish Notation.py 
# @Software: PyCharm
# ---------------------

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ("+", "*", "-", "/")
        res = 0
        for token in tokens:
            if token in operators:
                r = stack.pop()
                l = stack.pop()
                if token == "+":
                    res = l + r
                elif token == "-":
                    res = l - r
                elif token == "*":
                    res = l * r
                else:
                    res = abs(l) // abs(r)
                    if l * r < 0:
                        res *= -1
                token = res
            stack.append(int(token))
        return stack.pop()


