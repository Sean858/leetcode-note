#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/5 下午4:24 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 101. Symmetric Tree.py 
# @Software: PyCharm
# ---------------------


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        #     """
        #     :type root: TreeNode
        #     :rtype: bool
        #     """
        if not root:
            return True
        stack = []
        if root.left:
            if not root.right:
                return False
            else:
                stack.append(root.left)
                stack.append(root.right)
        else:
            if root.right:
                return False

        while stack:
            if len(stack) % 2 != 0:
                return False
            left = stack.pop()
            right = stack.pop()

            if left.val != right.val:
                return False

            if left.left:
                if not right.right:
                    return False
                else:
                    stack.append(left.left)
                    stack.append(right.right)
            else:
                if right.right:
                    return False

            if left.right:
                if not right.left:
                    return False
                else:
                    stack.append(left.right)
                    stack.append(right.left)
            else:
                if right.left:
                    return False
        return True

    def isSymmetric2(self, root):
        #     """
        #     :type root: TreeNode
        #     :rtype: bool
        #     """
        return root is None or self.isSymmetricHelp(root.left, root.right)
    def isSymmetricHelp(self, left, right):
        if left is None or right is None:
            return left == right
        if left.val != right.val:
            return False
        return self.isSymmetricHelp(left.left, right.right) and self.isSymmetricHelp(left.right, right.left)







