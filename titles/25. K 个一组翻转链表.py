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
            if count < k -1:
                dummy.next = p
                break
            else:
                dummy.next = q
                dummy = p
                p = temp
                count = 0
        return test
node = gen_list([1, 2, 3, 4, 5])
a = Solution().reverseKGroup(node, 3)
enum_node(a)
