#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/5 上午12:45 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 70. Climbing Stairs.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Non recursive
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a


#         Recursive with cache
#         cache = {}
#         return self.help(n, cache)

#     def help(self, n, cache):
#         if n == 0:
#             return 1
#         elif n < 0:
#             return 0
#         elif n in cache:
#             return cache[n]
#         else:
#             cache[n] = self.help(n - 1, cache) + self.help(n - 2, cache)
#             return cache[n]