#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/4 上午12:45 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 109. Convert Sorted List to Binary Search Tree.py 
# @Software: PyCharm
# ---------------------

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        fast, slow = head, head
        prev = ListNode(0)

        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        prev.next = None

        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root