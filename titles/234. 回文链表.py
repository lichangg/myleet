#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import ListNode,gen_list,enum_node

# 步骤1: 快慢指针找中点
# 步骤2: 反转链表
# 步骤3: 遍历两节对比
# tips: 在快慢指针找中点的时候实际上已经可以做反转链表的操作了
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        if not head.next.next:
            return head.val == head.next.val
        slow = head
        fast = head
        # 用快慢指针分成两部分
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        reverse_mid = self.reverseList(mid)
        while reverse_mid:

            if head.val != reverse_mid.val:
                return False
            head = head.next
            reverse_mid = reverse_mid.next
        return True
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        while cur:
            # 保存操作
            temp = cur.next
            # 逆转操作
            cur.next = pre

            #为下一个做准备
            pre = cur
            cur=temp
        return pre


# 这个就是在找中电的过程中顺便反转了前半部分的链表
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        pre, slow, fast = None, head, head
        while fast and fast.next:
            fast = fast.next.next
            temp = pre
            pre, slow = slow, slow.next
            pre.next = temp
        if fast:
            slow = slow.next
        while pre and pre.val == slow.val:
            slow = slow.next
            pre = pre.next
        return not pre

b=gen_list([1,0,0])
a=Solution().isPalindrome(b)
print(a)

