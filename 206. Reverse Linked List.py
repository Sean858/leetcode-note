#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/14 上午1:07 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 206. Reverse Linked List.py 
# @Software: PyCharm
# ---------------------

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

