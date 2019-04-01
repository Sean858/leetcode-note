#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/1 下午3:50 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 55. Jump Game.py 
# @Software: PyCharm
# ---------------------


# Greedy maybe the best way to fit this problem, O(n) and O(1)
# Max   3(3 + 0) 3(2 + 1) 3(1 + 2) 3(0 + 3) 3 < 4
# i     0 1 2 3

class Solution(object):
    def canJumpGreedy(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        Max = 0
        for i in range(len(nums)):
            if Max < i:
                return False
            Max = max(i + nums[i], Max)
        return True

    def main(self, nums):
        print self.canJumpGreedy(nums)
        # print self.canJumpDP(nums)

if __name__ == '__main__':
    nums = [3,2,1,0,4]
    Solution().main(nums)