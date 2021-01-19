#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from utils.util_funcs import ListNode,gen_list,enum_node

# 思路
# 1. 遍历链表并计数, 到第m个的时候记录下前一个node
# 2. 反转第m到n, 到n的时候记录下后一个node
# 3. 拼接三段
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m==n:
            return head
        count = 0
        ans = ListNode(0)
        ans.next = cur = head
        prefix = ans
        while cur and count<m-1:
            prefix=cur
            cur = cur.next
            count+=1

        reverse_count = 0
        rever_ans = ListNode(0)
        rever_ans.next = cur
        pre = None
        while cur and reverse_count<=n-m:
            nx = cur.next
            cur.next = pre

            pre = cur
            cur = nx
            reverse_count+=1

        # pre.next = cur
        rever_ans.next.next = cur
        prefix.next = pre

        return ans.next


b=gen_list([3,5])
a=Solution().reverseBetween(b,1,2)
enum_node(a)