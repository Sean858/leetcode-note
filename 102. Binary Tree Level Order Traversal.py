# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []

        def helper(node, level):
            if node:
                if len(levels) == level:
                    levels.append([])
                levels[level].append(node.val)
                helper(node.left, level + 1)
                helper(node.right, level + 1)

        helper(root, 0)
        return levels

#         ans = []
#         if not root:
#             return ans
#         level = [root]
#         while level:
#             ans.append([node.val for node in level])
#             temp = []
#             for node in level:
#                 temp.extend([node.left, node.right])
#             level = [leaf for leaf in temp if leaf]
#         return ans

