#!/usr/bin/env python
# -*- coding:utf-8 -*-

from utils.util_funcs import ListNode, gen_list,enum_node

class Solution:
    def mergeKLists(self, lists) -> ListNode:
        lists = list(filter(None,lists))
        if lists:
            lists.sort(key=lambda x:x.val)
            head = lists[0]
            lists[0] = head.next
            head.next = self.mergeKLists(lists)
            return head
l1 = gen_list([1,4,5])
l2 = gen_list([1,3,4])
l3 = gen_list([2,6])
a=Solution().mergeKLists([l1,l2,l3])
print(type(a))