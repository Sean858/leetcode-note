#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/19 下午2:24 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 567. Permutation in String.py 
# @Software: PyCharm
# ---------------------


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s2 or len(s1) > len(s2):
            return False
        count = [0] * 26
        for i in range(len(s1)):
            count[ord(s1[i]) - ord('a')] += 1
            count[ord(s2[i]) - ord('a')] -= 1
        if self.countZero(count):
            return True
        for i in range(len(s1), len(s2)):
            count[ord(s2[i]) - ord('a')] -= 1
            count[ord(s2[i - len(s1)]) - ord('a')] += 1
            if self.countZero(count):
                return True
        return False

    def countZero(self, count):
        for n in count:
            if n != 0:
                return False
        return True