#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/3 上午12:13 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 107. Binary Tree Level Order Traversal II.py 
# @Software: PyCharm
# ---------------------


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return None
        res = self.help([], root, 0)
        return res[::-1]

    def help(self, res, root, level):
        if not root:
            return None
        if level == len(res):
            res.append([])
        res[level].append(root.val)
        self.help(res, root.left, level + 1)
        self.help(res, root.right, level + 1)
        return res

#         res = []
#         if not root:
#             return res
#         q = collections.deque()
#         q.append(root)
#         res.append([root.val])

#         while q:
#             length = len(q)
#             temp = []
#             for _ in range(length):
#                 cur = q.popleft()
#                 if cur.left:
#                     q.append(cur.left)
#                     temp.append(cur.left.val)
#                 if cur.right:
#                     q.append(cur.right)
#                     temp.append(cur.right.val)
#             if temp:
#                 res.append(temp)
#         return res[::-1]
