#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/5/6 下午9:56
# @Author : Gaoxiang Chen
# @Site :
# @File : 4. Median of Two Sorted Arrays.py
# @Software: PyCharm
# ---------------------


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1
        imin, imax, median = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = median - i
            if i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            elif i < m and nums2[j - 1] > nums1[i]:
                imin = i + 1
            else:
                if i == 0:
                    left_max = nums2[j - 1]
                elif j == 0:
                    left_max = nums1[i - 1]
                else:
                    left_max = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return left_max

                if i == m:
                    right_min = nums2[j]
                elif j == n:
                    right_min = nums1[i]
                else:
                    right_min = min(nums1[i], nums2[j])

                return (left_max + right_min) / 2.0

