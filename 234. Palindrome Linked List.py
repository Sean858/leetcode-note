#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/14 下午8:47 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 234. Palindrome Linked List.py 
# @Software: PyCharm
# ---------------------


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        node = None
        while slow:
            temp = slow.next
            slow.next = node
            node = slow
            slow = temp
        while head and node:
            if head.val != node.val:
                return False
            head = head.next
            node = node.next
        return True
