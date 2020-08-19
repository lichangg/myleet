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



a=Solution().hasCycle(gen_list([3, 2, 0, -4]))