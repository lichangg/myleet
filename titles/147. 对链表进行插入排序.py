#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from utils.util_funcs import ListNode, gen_list, enum_node

# 一刷自己写的, 1500ms的级别, 其他python答案也都是这样, 不过下面的官方解答缩到了150ms级别, 暂时看不懂
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur = head
        new_head = ListNode(float('-inf'))
        while cur:
            temp = cur.next
            newcur = pre = new_head
            while newcur and cur.val > newcur.val:
                pre = newcur
                newcur = newcur.next
            pre.next = cur
            cur.next = newcur
            cur = temp

        return new_head.next

# 官方解答, 150ms级别
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        dummyHead = ListNode(0)
        dummyHead.next = head
        lastSorted = head
        curr = head.next

        while curr:
            if lastSorted.val <= curr.val:
                lastSorted = lastSorted.next
            else:
                prev = dummyHead
                while prev.next.val <= curr.val:
                    prev = prev.next
                lastSorted.next = curr.next
                curr.next = prev.next
                prev.next = curr
            curr = lastSorted.next

        return dummyHead.next


b = gen_list([4, 2, 1, 3])
# enum_node(rev(b))
a = Solution().insertionSortList(b)
enum_node(a)
