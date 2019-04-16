#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/14 下午11:20 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 236. Lowest Common Ancestor of a Binary Tree.py 
# @Software: PyCharm
# ---------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # condition
        if not root:
            return None
        if root == p or root == q:
            return root

        # divide
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # conquer
        if left and right:
            return root
        if not left:
            return right
        if not right:
            return left
