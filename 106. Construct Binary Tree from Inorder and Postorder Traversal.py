#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/2 下午11:48
# @Author : Gaoxiang Chen
# @Site :
# @File : 106. Construct Binary Tree from Inorder and Postorder Traversal.py
# @Software: PyCharm
# ---------------------


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder.pop())
        ind = inorder.index(root.val)
        root.right = self.buildTree(inorder[ind + 1:], postorder)
        root.left = self.buildTree(inorder[:ind], postorder)
        return root
