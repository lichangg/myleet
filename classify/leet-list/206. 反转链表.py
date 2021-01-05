#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import ListNode,gen_list,enum_node

# 思路：记录前节点就行了
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        while cur:
            nx = cur.next
            cur.next = pre
            pre =cur
            cur=nx
        return pre
b=gen_list([1,2,3,4,5])
a=Solution().reverseList(b)
enum_node(a)