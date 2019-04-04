#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/3 下午1:28 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 61. Rotate List.py 
# @Software: PyCharm
# ---------------------


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """


        # corner case
        if not head:
            return None
        if not head.next:
            return head

        # Two pointer
        fast = head
        slow = head
        length = 0

        # Get the length of list to determine k % length
        while fast:
            length += 1
            fast = fast.next

        # Set the fast to start status
        fast = head

        # Set the difference step between two pointers
        for i in range(k % length):
            fast = fast.next

        # Move together until fast get to the end
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Link the fast end to the head, so it is like a circle
        # Set the head to the slow.next, like 1,2,3,4,5, when the k = 2, slow will be 3 and fast will be 5
        fast.next = head
        # So we need seperate the 3 and 4, so the 4,5 could become the start of the new list
        head = slow.next
        # We should set the slow.next to None, like 3 -> Null
        slow.next = None

        return head



