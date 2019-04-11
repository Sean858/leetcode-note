#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/10 下午6:25 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 23. Merge k Sorted Lists.py 
# @Software: PyCharm
# ---------------------


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        # Compare
        dummy = ListNode(None)
        curr = dummy
        from Queue import PriorityQueue
        q = PriorityQueue()
        for node in lists:
            if node: q.put((node.val, node))
        while q.qsize() > 0:
            curr.next = q.get()[1]
            curr = curr.next
            if curr.next: q.put((curr.next.val, curr.next))
        return dummy.next

    def mergeKListsMergeSorr(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        med = len(lists) // 2
        left = self.mergeKLists(lists[:med])
        right = self.mergeKLists(lists[med:])
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
        res.next = left if left else right
        return dummy.next


