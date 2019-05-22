#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/1 下午11:09 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 394. Decode String.py 
# @Software: PyCharm
# ---------------------


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        num = ''
        curStr = ''
        for char in s:
            if char.isdigit():
                num += char
            elif char == '[':
                stack.append(num)
                stack.append(curStr)
                num = ''
                curStr = ''
            elif char == ']':
                preStr = stack.pop()
                mul = stack.pop()
                curStr = preStr + int(mul) * curStr
            else:
                curStr += char
        return curStr