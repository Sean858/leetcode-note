#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/10 上午10:16 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 21. Merge Two Sorted Lists.py 
# @Software: PyCharm
# ---------------------

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        dummy = ListNode(0)
        res = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next
            res = res.next

        res.next = l1 if l1 else l2

        return dummy.next

