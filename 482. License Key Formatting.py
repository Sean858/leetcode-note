#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/28 上午2:05 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 482. License Key Formatting.py 
# @Software: PyCharm
# ---------------------


class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        # ori = "".join(S.upper().split('-'))
        # res = []
        # for i in range(0, len(ori) // K):
        #     res.append(ori[len(ori) - (i + 1) * K : len(ori) - i * K])
        # if len(ori) % K != 0:
        #     res.append(ori[:len(ori) % K])
        # return "-".join(res[::-1])

        # if from 0 is confusing, can choose from other position

        ori = S.upper().replace('-', '')
        l = len(ori)
        size = K if l % K == 0 else l % K
        res = ori[:size]
        while size < l:
            res += '-' + ori[size: size + K]
            size += K
        return res