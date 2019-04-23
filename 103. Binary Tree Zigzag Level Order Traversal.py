#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/23 上午3:23 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 103. Binary Tree Zigzag Level Order Traversal.py 
# @Software: PyCharm
# ---------------------


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        deque = collections.deque()
        deque.append(root)
        level = 0

        while deque:
            temp = []
            size = len(deque)
            for i in range(size):
                node = deque.popleft()
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
                temp.append(node.val)
            res.append(temp if level % 2 == 0 else temp[::-1])
            level += 1
        return res

#         res = []
#         def dfs(root, res, level):
#             if root:
#                 if level == len(res):
#                     res.append([])
#                 if level % 2 == 0:
#                     res[level].append(root.val)
#                 else:
#                     res[level].insert(0, root.val)
#                 dfs(root.left, res, level + 1)
#                 dfs(root.right, res, level + 1)

#         dfs(root, res, 0)
#         return res
