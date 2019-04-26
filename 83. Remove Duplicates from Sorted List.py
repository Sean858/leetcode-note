#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/24 上午4:43 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 83. Remove Duplicates from Sorted List.py 
# @Software: PyCharm
# ---------------------


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        current = head.next
        prev = head

        while current:
            if current.val == prev.val:
                prev.next = current.next
                current = current.next
            else:
                current = current.next
                prev = prev.next
        return head


