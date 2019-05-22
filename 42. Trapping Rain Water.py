#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/10 下午10:14 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 42. Trapping Rain Water.py 
# @Software: PyCharm
# ---------------------


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        res = 0
        while left <= right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max <= right_max:
                res += left_max - height[left]
                left += 1
            else:
                res += right_max - height[right]
                right -= 1
        return res

    def trapStack(self, height):
        stack = []
        i, res = 0, 0
        while i < len(height):
            if not len(stack) or height[i] <= height[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                bottom = stack.pop()
                containWater = (min(height[stack[-1]], height[i]) - height[bottom]) * \
                               (i - stack[-1] - 1) if len(stack) else 0
                res += containWater
        return res


