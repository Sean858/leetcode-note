#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/18 下午4:20 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 678. Valid Parenthesis String.py 
# @Software: PyCharm
# ---------------------


# greed
# 1.
# // It's kind of confusing to explain the * == '' situation


class Solution:
    def checkValidString(self, s: str) -> bool:
        count = 0
        for c in s:
            if c == '(' or c == '*':
                count += 1
            else:
                if count <= 0:
                    return False
                count -= 1
        count = 0
        for c in s[::-1]:
            if c == ')' or c == '*':
                count += 1
            else:
                if count <= 0:
                    return False
                count -= 1
        return True


# 2.


class Solution:
    def checkValidString(self, s: str) -> bool:
        leftStack, starStack = [], []
        for i in range(len(s)):
            if s[i] == '(':
                leftStack.append(i)
            elif s[i] == '*':
                starStack.append(i)
            else:
                if leftStack:
                    leftStack.pop()
                elif starStack:
                    starStack.pop()
                else:
                    return False
        while leftStack and starStack:
            if leftStack.pop() > starStack.pop():
                return False
        return len(leftStack) == 0


# 3.
# Not good


def checkValidString(self, s: str) -> bool:
    def check(s, start, count):
        if count < 0:
            return False
        for i in range(start, len(s)):
            if s[i] == '(':
                count += 1
            elif s[i] == ')':
                if count <= 0:
                    return False
                count -= 1
            else:
                return check(s, i + 1, count) or check(s, i + 1, count + 1) or check(s, i + 1, count - 1)
        return count == 0

    return check(s, 0, 0)