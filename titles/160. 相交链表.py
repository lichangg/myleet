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

# 别人写的, 也太优雅了, 学到了,
# 思路就是A指针和B指针分别从headA和headB头节点出发, 哪个指针走完之后换到另一个头节点继续走,也就是:
# A走了len(headA) + len(headB)
# B走了len(headB) + len(headA)
# 两者长度肯定是一样长的
# 情况1: headA和headB不相交, 那么结束于None=None位置, 返回None
# 情况2: headA和headB相交, 那肯定结束于交点位置,返回交点
# 土味理解: 假如headA是长链表,headB是短链表, 指针A,B同时分别从headA和headB出发, 由于任意时间点AB走过的路程都一样, AB必定会在走完各自最先走的节点然后换节点走的时候相遇在交点(因为速度一样,路程一样, 肯定会同时到达交点)
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        ha, hb = headA, headB
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        return ha

# 二刷, 需要注意一些小细节,不过这个方法用了额外的空间
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        sa=set()
        sb=set()
        while 1:
            if headA in sb:
                return headA
            sa.add(headA)
            if headB in sa:
                return headB
            sb.add(headB)
            if headA:
                headA = headA.next
            if headB:
                headB = headB.next
            if not headA and not headB:
                return