#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/4 上午2:14 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 111. Minimum Depth of Binary Tree.py 
# @Software: PyCharm
# ---------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = root.left
        right = root.right
        if not left and not right:
            return 1
        min_depth = float('inf')
        if left:
            min_depth = min(self.minDepth(root.left), min_depth)
        if right:
            min_depth = min(self.minDepth(root.right), min_depth)
        return min_depth + 1
