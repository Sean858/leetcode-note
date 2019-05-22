#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/15 上午2:02 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 297. Serialize and Deserialize Binary Tree.py 
# @Software: PyCharm
# ---------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = ""
        if not root:
            return res
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if node:
                res += " " + str(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                res += " None"
        return res.strip()

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nodes = collections.deque(data.split())
        n = nodes.popleft()
        root = None if n == 'None' else TreeNode(int(n))
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if node:
                a, b = nodes.popleft(), nodes.popleft()
                node.left = TreeNode(int(a)) if a != 'None' else None
                node.right = TreeNode(int(b)) if b != 'None' else None
                q.append(node.left)
                q.append(node.right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))



# DFS

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def help(node):
            if node:
                vals.append(str(node.val))
                help(node.left)
                help(node.right)
            else:
                vals.append('#')

        vals = []
        help(root)
        return ','.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def help():
            node = next(nodes)
            if node == '#':
                return None
            root = TreeNode(int(node))
            root.left = help()
            root.right = help()
            return root

        nodes = iter(data.split(','))
        return help()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))