#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import ListNode, gen_list, enum_node
# K 个一组翻转链表
'''
思路:
1. 先写出每k个反转一次的方法
2. 每k个反转之后拼接
'''
class Solution:
    def rever(self,head, k):
        i = 0
        ans = ListNode(0)
        ans.next = head
        tmp_count = head
        pre = None
        count = 0
        while tmp_count and count <= k:
            count += 1
            tmp_count = tmp_count.next
        if count < k:
            return head

        while i <= k - 1 and head != None:
            nex = head.next

            head.next = pre
            pre = head
            head = nex
            i += 1
        return pre, ans.next, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def recur(pre_tail, head):
            tp = self.rever(head, k)
            if head == None:
                return
            if isinstance(tp, ListNode):
                pre_tail.next = head
                return
            new_h, tail, nx = tp
            pre_tail.next = new_h
            recur(tail, nx)
            return new_h

        return recur(ListNode(0), head)




if __name__ == "__main__":
    b = gen_list([1, 2, 3,4,5,6,7,8,9])
    # tp = rever(b, 7)
    # if isinstance(tp, ListNode):
    #     enum_node(tp)
    # else:
    #     a, t, nx = tp
    #     enum_node(a)
    #     enum_node(t)
    #     enum_node(nx)
    a=Solution().reverseKGroup(b, 3)
    enum_node(a)