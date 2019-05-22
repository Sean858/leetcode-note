#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/30 上午1:50 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 82. Remove Duplicates from Sorted List II.py 
# @Software: PyCharm
# ---------------------

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = prev = ListNode(0)
        cur = head
        dummy.next = cur
        while cur:
            if cur.next and cur.next.val == cur.val:
                while cur.next and cur.next.val == cur.val:
                    cur = cur.next
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next

        return dummy.next