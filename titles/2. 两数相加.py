#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 整个流程是从链头(也就是个位数)依次往高位计算并带上进位
from utils.util_funcs import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, carry=0) -> ListNode:
        if l1 == None and l2 == None and carry == 0:
            return None

        if l1 == None and l2 == None and carry == 1:
            return ListNode(1)

        # l1和l2长度不相等的情况
        if l1 == None:
            l1 = ListNode(0)
        if l2 == None:
            l2 = ListNode(0)

        # l1.val + l2.val + carry 这三个值相加小于20, 商只有0,1两个取值
        carry, l1.val = divmod(l1.val + l2.val + carry, 10)
        l1.next = self.addTwoNumbers(l1.next, l2.next, carry)

        return l1