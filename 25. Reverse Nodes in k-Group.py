#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/5/1 上午12:02 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 25. Reverse Nodes in k-Group.py 
# @Software: PyCharm
# ---------------------


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = prev = ListNode(0)
        fast, slow = head, head
        dummy.next = slow
        step = 1

        while fast:
            step = 0
            while step < k and fast:
                fast = fast.next
                step += 1
            if step == k:
                for _ in range(k):
                    temp = slow.next
                    slow.next = prev
                    prev = slow
                    slow = temp
                    print slow.val
            else:
                for _ in range(step):
                    slow = slow.next
        return dummy.next


def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def stringToInt(input):
    return int(input)


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            head = stringToListNode(line)
            line = lines.next()
            k = stringToInt(line)

            ret = Solution().reverseKGroup(head, k)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()