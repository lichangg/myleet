#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 要仔细考虑删除第一个和最后一个的特殊情况
# 执行用时：48 ms, 在所有 Python3 提交中击败了34.08%的用户
# 内存消耗：13.8 MB, 在所有 Python3 提交中击败了18.65%的用户
# 思路就是用hashmap存下每一个节点，key为index，直接将第len(hashmap) - n-1的next指向len(hashmap) - n + 1
# 第len(hashmap) - n个就直接丢掉了， 这个思路只用遍历一次
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         index=0
#         hashmap = {}
#         if not head.next:
#             return
#         while head:
#             hashmap[index] = head
#             index +=1
#             head = head.next
#         if len(hashmap) ==n:
#             return hashmap[1]
#         if n == 1:
#             hashmap[len(hashmap)-2].next =  None
#             return hashmap[0]
#         hashmap[len(hashmap) - n-1].next = hashmap[len(hashmap) - n + 1]
#
#         return hashmap[0]

# 别人的方法, 可以设置一个虚拟指针, 后面的有点看不懂
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 设置虚拟指针的目的是防止删除第一个节点
        dum = ListNode(0)
        dum.next = head
        cur = head
        pre = dum

        # 先走n步
        for _ in range(n):
            cur = cur.next
        # 再走剩余的步，最后pre指向的就是要删除节点的前面一个节点,这一步看不懂
        while cur:
            cur = cur.next
            pre = pre.next

        # 删除这个节点
        pre.next = pre.next.next

        return dum.next

# 二刷时的思路更low一点,想着先遍历一遍统计出链表的总数，再遍历一遍进行删除。。。
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        count = 0

        while head:
            count +=1
            head = head.next

nodes=[ListNode(i) for i in [1,2]]
for index, i in enumerate(nodes):
    i.next = nodes[index+1] if index<len(nodes)-1 else None

myhead=Solution().removeNthFromEnd(nodes[0],1)
while myhead:
    print(myhead.val)
    myhead = myhead.next