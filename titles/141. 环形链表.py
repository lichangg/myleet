#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import ListNode, gen_list


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        set1 = set()
        while head:
            head = head.next
            if head in set1:
                return True

            set1.add(head)
        return False

# 此方法空间复杂度为O(1),学到了
# 快慢指针，快指针每次走两步，慢指针走一步
# 当快慢指针相遇，说明存在环
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

a=Solution().hasCycle(gen_list([3, 2, 0, -4]))