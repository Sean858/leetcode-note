#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/18 下午4:20 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 384. Shuffle an Array.py 
# @Software: PyCharm
# ---------------------


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        nums = self.nums[:]
        for i in range(len(nums)):
            j = random.randrange(len(nums))
            nums[i], nums[j] = nums[j], nums[i]
        return nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()