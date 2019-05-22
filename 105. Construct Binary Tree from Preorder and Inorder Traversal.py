#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/1 下午7:44 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 105. Construct Binary Tree from Preorder and Inorder Traversal.py 
# @Software: PyCharm
# ---------------------

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[:ind])
            root.right = self.buildTree(preorder, inorder[ind + 1:])
            return root
