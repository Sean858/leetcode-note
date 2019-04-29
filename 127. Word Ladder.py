#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/8 下午11:41 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 127. Word Ladder.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        import collections
        queue = collections.deque([beginWord])
        wordSet = set([])
        for word in wordList:
            wordSet.add(word)
        distance = 0

        while queue:
            distance += 1
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return distance
                for nextWord in self.getNextWord(word):
                    if nextWord in wordSet:
                        queue.append(nextWord)
                        wordSet.remove(nextWord)
        return 0

    def getNextWord(self, word):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                words.append(left + char + right)
        return words
