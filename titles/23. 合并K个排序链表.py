#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

from utils.util_funcs import ListNode, gen_list, enum_node

# 这种解法也是很自然能想到,只不过在sort那一步时间复杂度倍增了
class Solution:
    def mergeKLists(self, lists) -> ListNode:
        lists = list(filter(None, lists))
        if lists:
            lists.sort(key=lambda x: x.val)
            head = lists[0]
            lists[0] = head.next
            head.next = self.mergeKLists(lists)
            return head



# 二刷时自己写的递归的小根堆的方法
# 这种题目看到就很自然的想到小根堆
# 不过比后面那个别人写的多出了一倍的空间,暂时不知道哪儿出了问题
# 小根堆的pop和push复杂度都为O(logN) 存疑
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(0)
        hq = []

        def recur(hq, cur, lists):
            if not hq:
                return
            val, idx = heapq.heappop(hq)
            cur.next = lists[idx]
            if lists[idx].next:
                lists[idx] = lists[idx].next
                heapq.heappush(hq, [lists[idx].val, idx])
            recur(hq, cur.next,lists)

        for index, per_node in enumerate(lists):
            if per_node:
                heapq.heappush(hq, [per_node.val, index])
        recur(hq, dummy, lists)
        return dummy.next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        dummy = ListNode(-1)
        p = dummy
        head = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(head, [lists[i].val, i])
                lists[i] = lists[i].next
        while head:
            val, idx = heapq.heappop(head)
            node = ListNode(val)
            p.next = node
            p = p.next
            if lists[idx]:
                heapq.heappush(head, [lists[idx].val, idx])
                lists[idx] = lists[idx].next
        return dummy.next
l2 = gen_list([1])
l3 = gen_list([2, 6])
a = Solution().mergeKLists([l2, l3])
print(enum_node(a))
