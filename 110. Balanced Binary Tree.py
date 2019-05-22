#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/4 上午1:18 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 110. Balanced Binary Tree.py 
# @Software: PyCharm
# ---------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.bst(root) != -1

    def bst(self, root):
        if not root:
            return 0

        left = self.bst(root.left)
        right = self.bst(root.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)


