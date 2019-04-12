#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/12 上午1:26 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 160. Intersection of Two Linked Lists.py 
# @Software: PyCharm
# ---------------------


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 这两个什么区别，
# while A.next:
#   A = A.next
# A.next = B

# while A:
#   A = A.next
# A = B


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        listA = headA
        listB = headB

        while listA != listB:
            listA = listA.next if listA else headB
            listB = listB.next if listB else headA
        return listA