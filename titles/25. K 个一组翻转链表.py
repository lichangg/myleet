#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 二刷失败, 想的头晕
from utils.util_funcs import ListNode, gen_list, enum_node


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        p = head
        count = 0
        test = head.next.next
        while p:
            q = p.next
            temp = q.next
            while temp and temp.next:
                temp11, temp.next = temp.next, q
                q, temp = temp, temp11
                count += 1
                if count == k - 1:
                    break
            if count < k - 1:
                dummy.next = p
                break
            else:
                dummy.next = q
                dummy = p
                p = temp
                count = 0
        return test


# 再刷
# 1. 先计数, 不够k就直接返回了
# 2. 若节点数可够反转,那就开始进行反转
#     - 虚节点始终指向反转之后的头节点
#     - 原来的头节点指向下一个[要反转的节点区间]
#     - 用一个变量计数反转了多少个
# 3. 结束
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        if count < k:
            return head

        dummy = ListNode(0)
        count_reverse = 0
        pre = None
        cur = head
        while cur and count_reverse < k:
            tmp = cur.next
            cur.next = pre

            pre= cur
            cur = tmp
            count_reverse+=1
        dummy.next = pre
        head.next = self.reverseKGroup(cur, k)

        return dummy.next


node = gen_list([1, 2, 3, 4, 5])
a = Solution().reverseKGroup(node, 3)
enum_node(a)
