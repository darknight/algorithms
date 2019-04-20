#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node is None:
            return
        curr = node.next
        while curr.next:
            node.val = curr.val
            node = curr
            curr = curr.next
        node.val = curr.val
        node.next = None
        del curr
