#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/12 上午12:16 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 141. Linked List Cycle.py 
# @Software: PyCharm
# ---------------------


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Why this is problem has a value pos?????
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False