#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import ListNode, gen_list,enum_node

# 思路：快慢指针找到中点，用一个数组存前半段的值，用中点之后的节点值和该数组的元素比较
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:return True
        slow = fast = head
        pre = []
        while fast.next and fast.next.next:
            pre.append(slow.val)
            fast = fast.next.next
            slow = slow.next
        if fast.next:
            pre.append(slow.val)
        mid = slow.next
        idx = len(pre)-1
        while mid:
            if mid.val != pre[idx]:
                return False
            else:
                mid=mid.next
                idx-=1

        return True

b=gen_list([1,3,3,1])
a=Solution().isPalindrome(b)
print(a)