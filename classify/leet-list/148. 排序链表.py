#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import ListNode, enum_node,gen_list

# 思路1：
# 1. 递归从中点将链表拆成左右两边l和r
# 2. 拆到最小细粒度后归并
class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        fast = slow = head
        if not head or not head.next :
            return head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        tmp = slow.next
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(tmp)
        return self.mergeTwoLists(l, r)
    def merge(self, l, r):
        ans = ListNode(0)
        if l.val > r.val:
            head = r
        else:
            head = l
        cur = head
        ans.next = head

        while l.next and r.next:
            if cur.val > l.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r =r.next
            cur = cur.next
        if l.next:
            cur.next = l
        elif r.next:
            cur.next = r
        else:
            cur.next = None

        return ans.next
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2  # 终止条件，直到两个链表都空
        if not l2: return l1
        if l1.val <= l2.val:  # 递归调用
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
b=[4,2,1,3]
b=gen_list(b)
a=Solution().sortList(b)
enum_node(a)