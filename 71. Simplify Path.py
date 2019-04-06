#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/6 上午2:27 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 71. Simplify Path.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        valid = []
        res = ''
        pathArr = path.strip().split('/')

        for word in pathArr:
            if word == '..':
                if valid:
                    valid.pop()
            elif word == '.' or not word:
                continue
            else:
                valid.append(word)

        return "/" + "/".join(valid)
