#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/3 上午1:29 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 108. Convert Sorted Array to Binary Search Tree.py 
# @Software: PyCharm
# ---------------------


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root


