#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import ListNode,gen_list

# 迭代
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        if not l1 or not l2:return l1 or l2
        if l1.val<l2.val:
            dummy.next = l1
            l1 = l1.next
        else:
            dummy.next = l2
            l2 = l2.next
        cur = dummy.next
        while l1 and l2:
            while l1 and l2 and l1.val <= l2.val:
                cur.next = l1
                cur = cur.next

                l1 = l1.next
            while l1 and l2 and l2.val < l1.val:
                cur.next = l2
                cur = cur.next

                l2 = l2.next
        if not l1:
            cur.next = l2
        if not l2:
            cur.next = l1
        return dummy.next

# 还是递归香
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:return l1 or l2

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

a=gen_list([])
b=gen_list([])
c=Solution().mergeTwoLists(a,b)