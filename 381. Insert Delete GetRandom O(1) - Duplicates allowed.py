#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/18 下午7:47 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 381. Insert Delete GetRandom O(1) - Duplicates allowed.py 
# @Software: PyCharm
# ---------------------

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.res = []
        self.dict = collections.defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        temp = False
        if val not in self.dict or not self.res:
            temp = True
        self.res.append(val)
        self.dict[val].add(len(self.res) - 1)
        return temp

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.dict or not self.res:
            return False
        i_last = len(self.res) - 1
        index, last = self.dict[val].pop(), self.res[-1]
        self.res[index] = last
        self.res.pop()
        self.dict[last].add(index)
        self.dict[last].remove(i_last)

        if len(self.dict[val]) == 0:
            self.dict.pop(val)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return self.res[random.randrange(len(self.res))]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()