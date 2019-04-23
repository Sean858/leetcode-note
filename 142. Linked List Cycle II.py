#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/23 上午2:16 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 142. Linked List Cycle II.py 
# @Software: PyCharm
# ---------------------


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Set => Hashset()
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        visited = set()
        while head:
            if head in visited:
                return head
            else:
                visited.append(head)
                head = head.next
        return None

        # slow, fast = head, head
        # while slow and fast:
        #     if slow.next:
        #         slow = slow.next
        #     if fast.next.next:
        #         fast = fast.next.next
        #     if fast == slow:
        #         return fast
        # return None
