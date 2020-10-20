#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from utils.util_funcs import ListNode,enum_node

# 这个问题好无聊啊.
# 因为链表无法根据下标访问,但是list可以, 直接把链表转为list,然后再做出链表就行了
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return

        vec = list()
        node = head
        while node:
            vec.append(node)
            node = node.next

        i, j = 0, len(vec) - 1
        while i < j:
            vec[i].next = vec[j]
            i += 1
            if i == j:
                break
            vec[j].next = vec[i]
            j -= 1

        vec[i].next = None


a=Solution().reorderList()
enum_node(a)