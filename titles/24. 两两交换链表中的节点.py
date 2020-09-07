#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import ListNode, gen_list,enum_node
# 执行用时：32 ms, 在所有 Python3 提交中击败了97.57%的用户
# 内存消耗：13.7 MB, 在所有 Python3 提交中击败了48.89%的用户
# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         if not head:
#             return
#         if not head.next:
#             return head
#         dummy = ListNode(-1)
#         dummy.next = head
#         b = head.next
#         res = head.next
#         while dummy.next and dummy.next.next:
#             head.next =b.next
#             b.next, dummy.next = head,b
#
#             dummy = head
#             head= dummy.next
#             if not head:
#                 break
#             b = head.next
#
#         return res

# 别人的更简洁的写法
# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         thead = ListNode(-1)
#         thead.next = head
#         c = thead
#         while c.next and c.next.next:
#             a, b=c.next, c.next.next
#             c.next, a.next = b, b.next
#             b.next = a
#             c = c.next.next
#         return thead.next

#别人的方法,此方法更加通用一点, 更换target可以实现每target个节点进行一次倒叙
# 这个很精妙,题目虽然是每两个互换, 这个可以实现每target个互换
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        l1 = ListNode(-1)
        target = 2
        p = l1
        count = 0
        while head and count < target:
            q = head
            head = head.next
            q.next = p.next
            p.next = q
            count += 1
            if count == target:
                while p.next:
                    p = p.next
                count = 0
        return l1.next

# 二刷时,还是费劲想..太绕了,头晕
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        node1 = head
        # 保存一下头部节点,这个很重要
        res = head.next
        if not head:
            return
        while node1 and node1.next:
            temp = node1.next.next
            dummy.next = node1.next
            node1.next.next = node1

            if not temp or not temp.next :
                node1.next = temp
                break
            dummy = node1
            node1 = temp

        return res or head

node=gen_list([1])
a=Solution().swapPairs(node)
enum_node(a)