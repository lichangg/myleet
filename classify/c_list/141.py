#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import ListNode

# 思路1: 用dict存走过的节点

# 思路2: 有环必定相遇
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True

