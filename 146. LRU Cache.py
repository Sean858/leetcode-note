#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/9 下午9:43 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 146. LRU Cache.py 
# @Software: PyCharm
# ---------------------

class DoubleLinkedList:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.post = None


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = {}
        self.head = doublelinkedlist(0, 0)
        self.tail = doublelinkedlist(0, 0)
        self.head.post = self.tail
        self.tail.prev = self.head

    def removenode(self, node):
        prev = node.prev
        post = node.post
        prev.post = post
        post.prev = prev

    def addnode(self, node):
        node.prev = self.head
        node.post = self.head.post
        self.head.post.prev = node
        self.head.post = node

    def movetohead(self, node):
        self.removenode(node)
        self.addnode(node)

    def poptail(self):
        node = self.tail.prev
        self.removenode(node)
        return node

    def get(self, key):
        if key not in self.dict:
            return -1
        node = self.dict[key]
        self.removenode(node)
        self.movetohead(node)
        return node.val

    def put(self, key, value):
        if key not in self.dict:
            newnode = doublelinkedlist(key, value)
            self.addnode(newnode)
            self.dict[key] = newnode
            if len(self.dict) > self.capacity:
                tail = self.poptail()
                self.dict.pop(tail.key)
        else:
            node = self.dict[key]
            self.dict[key].val = value
            self.movetohead(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)