#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/12 下午8:55 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 199. Binary Tree Right Side View.py 
# @Software: PyCharm
# ---------------------


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #       DFS
        res = []
        if not root:
            return res
        self.dfs(root, res, 0)
        return res

    def dfs(self, root, res, h):
        if root == None:
            return
        if h == len(res):
            res.append(root.val)
        self.dfs(root.right, res, h + 1)
        self.dfs(root.left, res, h + 1)

    def bfs(self, root):
        if not root:
            return []
        deque = collections.deque()
        deque.append(root)
        res = []

        while deque:
            size = len(deque)
            for i in range(size):
                cur = deque.popleft()
                if i == size - 1:
                    res.append(cur.val)
                if cur.left:
                    deque.append(cur.left)
                if cur.right:
                    deque.append(cur.right)
        return res
