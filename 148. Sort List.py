#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/2 上午12:58
# @Author : Gaoxiang Chen
# @Site :
# @File : 148. Sort List.py
# @Software: PyCharm
# ---------------------

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        prev = ListNode(0)
        slow, fast = head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # split the list
        prev.next = None

        left = self.sortList(head)
        right = self.sortList(slow)

        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode(0)
        res = dummy
        while left and right:
            if left.val <= right.val:
                res.next = left
                left = left.next
            else:
                res.next = right
                right = right.next
            res = res.next
        if left:
            res.next = left
        if right:
            res.next = right
        return dummy.next
