#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 旋转链表

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from utils.util_funcs import ListNode,gen_list,enum_node

"""
思路
1. 先获取链表长度l
2. k/l取余mod得到头节点会在倒数第mod个
3. 倒数第mod+1个节点指向None, tail节点指向head, 返回mod节点
"""
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        count = 0
        ans = ListNode(0)
        ans.next = head
        tail = head

        while head:
            tail = head
            head = head.next
            count +=1
        tail.next = ans.next

        div, mod = divmod(k, count)

        i = 0
        cur = tmp = ans.next

        while i<count-mod:
            tmp = cur
            cur = cur.next
            i+=1
        tmp.next = None
        return cur
a=gen_list([])
Solution().rotateRight(a,12)
