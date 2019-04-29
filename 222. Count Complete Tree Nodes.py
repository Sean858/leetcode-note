#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/29 上午12:24 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 222. Count Complete Tree Nodes.py 
# @Software: PyCharm
# ---------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getHeight(self, root):
        if not root:
            return 0
        res = 0
        while root:
            res += 1
            root = root.left
        return res

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        if not root:
            return res
        while root:
            l, r = map(self.getHeight, (root.left, root.right))
            if l == r:
                res += 1 << l
                root = root.right
            else:
                res += 1 << r
                root = root.left
        return res

        # if not root:
        #     return 0
        # q = collections.deque([root])
        # res = 0
        # while q:
        #     cur = q.popleft()
        #     res += 1
        #     if cur.left:
        #         q.append(cur.left)
        #     if cur.right:
        #         q.append(cur.right)
        # return res


