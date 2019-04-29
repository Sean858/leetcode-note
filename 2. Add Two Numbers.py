#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/9 下午4:06 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 2. Add Two Numbers.py 
# @Software: PyCharm
# ---------------------

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        plus = 0
        root = n = ListNode(0)

        while l1 or l2 or plus:
            v1, v2 = 0, 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            plus, res = divmod(v1 + v2 + plus, 10)
            n.next = ListNode(res)
            n = n.next

        return root.next

