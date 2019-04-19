#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/19 上午1:13 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 380. Insert Delete GetRandom O(1).py 
# @Software: PyCharm
# ---------------------

class RandomizedSet(object):

    # [] O(1)操作的实现，{} and [], when remove, change index of target val with the last val, and pop,
    # also hash has pop operation.
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.res, self.Map = [], {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.Map:
            self.res.append(val)
            self.Map[val] = len(self.res) - 1
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.Map:
            index, last = self.Map[val], self.res[-1]
            self.res[index], self.Map[last] = last, index
            self.res.pop()
            self.Map.pop(val, 0)
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.res[random.randint(0, len(self.res) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()