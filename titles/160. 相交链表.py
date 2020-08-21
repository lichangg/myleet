#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 如果两个链表没有交点，返回 null.
# 在返回结果后，两个链表仍须保持原有的结构。
# 可假定整个链表结构中没有循环。
# 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

from utils.util_funcs import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        newheadA=headA
        newheadB=headB
        countA = 0
        countB = 0
        while headA or headB:
            if headA and headB:
                headA = headA.next
                headB = headB.next
            elif headA:
                headA = headA.next
                countA+=1
            else:
                headB = headB.next
                countB+=1

        longer_node = newheadA if countA else newheadB
        short_node = newheadA if countB else newheadB

        for _ in range(countA or countB):

            longer_node = longer_node.next

        while longer_node:
            if longer_node == short_node:
                return longer_node
            longer_node = longer_node.next
            short_node = short_node.next

        return None

# 别人写的, 也太优雅了, 学到了
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        ha, hb = headA, headB
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        return ha
