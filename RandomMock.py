#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/11 上午10:58 
# @Author : Gaoxiang Chen
# @Site :  
# @File : RandomMock.py
# @Software: PyCharm
# ---------------------

import random

class Random:
    def random_int_list(self, list, k):
        return random.sample(list, k)

print(Random().random_int_list([1, 2, 3, 4, 5], 5))


