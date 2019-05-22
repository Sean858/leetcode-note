#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/18 上午12:55 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 143. Reorder List.py 
# @Software: PyCharm
# ---------------------

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def findMid(head):
            slow, fast = head, head
            prev = ListNode(0)
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = None
            return (head, slow)

        def reverse(mid):
            prev = None
            cur = mid
            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev

        def merge(head, prev):
            res = ListNode(0)
            cur = head
            while cur:
                if cur:
                    res.next = cur
                    cur = cur.next
                    res = res.next
                if prev:
                    res.next = prev
                    prev = prev.next
                    res = res.next

        if not head or not head.next:
            return
        head, mid = findMid(head)
        reversedMid = reverse(mid)
        merge(head, reversedMid)







