#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/12 上午12:58 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 155. Min Stack.py 
# @Software: PyCharm
# ---------------------

# 构建数据结构的题也很重要，思想
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.q.append((x, curMin))

    def pop(self):
        """
        :rtype: None
        """
        self.q.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.q) == 0:
            return None
        return self.q[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.q) == 0:
            return None
        return self.q[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()