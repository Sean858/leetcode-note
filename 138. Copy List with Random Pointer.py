#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/9 下午10:57 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 138. Copy List with Random Pointer.py 
# @Software: PyCharm
# ---------------------

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution(object):
    def copyRandomListWithMap(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # Map Solution
        # 1 - c1
        # 2 - c2
        # 3 - c3
        # if 1.next = 2 => c1.next = c2
        # if 1.random = 2 => c1.random = c2
        if not head:
            return None
        Map = {}
        node = head
        while node:
            Map[node] = Node(node.val, None, None)
            node = node.next
        node = head
        while node:
            Map[node].next = Map[node.next] if node.next else None
            Map[node].random = Map[node.random] if node.random else None
            node = node.next
        return Map[head]

    def copyRandomListWithoutMap(self, head):
        # Copy List Solution
        # 1 - c1 - 2 - c2 - 3 - c3
        if not head:
            return None
        node = head
        while node:
            copy = Node(node.val, None, None)
            copy.next = node.next
            node.next = copy
            node = node.next.next
        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next

        node = head
        dummy = head.next
        prev = head.next
        while node:
            node.next = node.next.next
            node = node.next
            if prev.next:
                prev.next = node.next
            prev = prev.next
        return dummy





