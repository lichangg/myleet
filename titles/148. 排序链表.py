#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import ListNode,gen_list,enum_node
import time
# 自己写的,超时
# class Solution:
#     def sortList(self, head: ListNode) -> ListNode:
#         if not head:
#             return head
#         temp = head.next
#         head.next = None
#         while temp:
#             cur = head
#             pre = None
#             while cur:
#                 if cur.val>=temp.val:
#                     break
#                 pre = cur
#                 cur = cur.next
#             n = temp.next
#             if pre:
#                 pre.next = temp
#                 temp.next = cur
#             else:
#                 temp.next = head
#                 head = temp
#             temp = n
#         return head


# 惊了, 快速找到链表的中间节点可以用快慢指针的方法,学到了
# 慢指针一次移动一个节点,快指针一次移动两个,当快指针走完的时候慢指针所在的节点就是中间节点(不过这里要注意的是[该节点的下一个节点才是右半部分的起点]),复杂度为O(n)
# 此算法主要是归并的思想
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow = head
        fast = head
        # 用快慢指针分成两部分
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # 找到左右部分, 把左部分最后置空,这一步是在划分左右用以之后的分别递归
        mid = slow.next
        slow.next = None
        # 递归下去
        left = self.sortList(head)
        right = self.sortList(mid)
        # 合并
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode(0)
        p = dummy
        l = left
        r = right

        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
                p = p.next
            else:
                p.next = r
                r = r.next
                p = p.next
        # 因为循环退出了,所以下面这两个条件始终只有一个成立
        if l:
            p.next = l
        if r:
            p.next = r
        return dummy.next

# 二刷彻底失败
# class Solution:
#     def sortList(self, head: ListNode) -> ListNode:
#         dummy = ListNode(0)
#         dummy.next = head
#         cur = head
#         temp = cur.next.next
#         while cur.next:
#             if cur.next.val<cur.val:
#                 dummy.next = cur.next
#                 cur.next.next = cur
#                 cur.next = temp
#             else:
#                 cur=cur.next
#             if not temp:
#                 break
#             dummy = dummy.next
#             temp = temp.next
#         return head
# b=gen_list([1,3,3,1,3,1,3,3,2,3,2,2,1,1,1,3,2,2,1,1,2,2,2,3,3,1,1,2,2,2,1,2,1,1,2,3,3,2,2,3,2,3,2,2,2,1,1,3,2,3,3,1,1,1,2,2,1,2,2,2,2,3,1,3,1,1,1,2,1,2,2,2,1,3,2,2,2,3,3,2,3,3,1,1,2,2,1,2,1,3,2,1,3,3,1,2,1,1,1,1,1,2,1,2,2,2,2,3,3,3,1,1,3,2,1,1,2,1,3,3,2,2,1,3,1,3,1,3,2,2,3,2,3,2,2,1,2,3,1,3,1,2,3,3,2,3,3,3,1,1,2,3,1,2,3,2,1,1,2,3,1,1,3,1,2,2,3,2,1,3,1,2,1,3,2,1,1,2,2,2,1,3,1,3,2,3,3,1,1,3,1,2,1,2,3,1,2,1,1,3,1,3,3,1,1,1,2,2,1,3,1,2,2,3,2,1,3,2,1,3,2,2,3,3])
b=gen_list([1,2,5,4,3])
start = time.time()
a=Solution().sortList(b)
# print(time.time() - start)
#0.001982450485229492  0.0009980201721191406 0.001995086669921875
enum_node(a)