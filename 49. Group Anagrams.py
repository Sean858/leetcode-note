#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/9 下午8:10 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 49. Group Anagrams.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        # If we don't use sorted word as key,
        # we can use defaultdict to set a default, like []
        words = {}
        res = []
        for s in strs:
            # In python, when sort string, it seperate the string with ,
            # print(sorted(s))
            # [u'a', u'e', u't']
            temp = ''.join(sorted(s))
            if temp in words:
                words[temp].append(s)
            else:
                words[temp] = [s]

        for key in words:
            res.append(words[key])
        return res

    def groupAnagramsUseTuple(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

    def groupAnagramsByCount(strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()