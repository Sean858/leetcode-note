#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/13 下午1:34 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 204. Count Primes.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        prime = [1] * n
        prime[0] = prime[1] = 0

        for i in range(2, int(n ** 0.5) + 1):
            # if prime[i]:
            #     for j in range(i, (n - 1) // i + 1):
            #         prime[i * j] = 0
            prime[i * i: n: i] = [0] * ((n - 1 - i * i) // i + 1)
        return sum(prime)

#         if n <= 2:
#             return 0
#         prime = [True] * (n + 1)
#         prime[0] = prime[1] = False
#         res = 0

#         for i in range(2, n):
#             if prime[i]:
#                 res += 1
#                 for j in range(i, n // i + 1):
#                     prime[i * j] = False
#         return res

# if n <= 2:
#     return 0
# res = 1
# for i in range(3, n):
#     for j in range(2, int(i ** (1.0 / 2)) + 1):
#         if i % j == 0:
#             res -= 1
#             break
#     res += 1
# return res
