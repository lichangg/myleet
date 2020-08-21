#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import ListNode,gen_list,enum_node
# 基础题  要掌握啊!!!
#这是迭代的方法
# 执行用时：40 ms, 在所有 Python3 提交中击败了90.94%的用户
# 内存消耗：14.6 MB, 在所有 Python3 提交中击败了55.51%的用户
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         cur = head
#         pre = None
#         while cur:
#             # 保存操作
#             temp = cur.next
#             # 逆转操作
#             cur.next = pre
#
#             #为下一个做准备
#             pre = cur
#             cur=temp
#         return pre

# 递归的方法
# 执行用时：44 ms, 在所有 Python3 提交中击败了76.86%的用户
# 内存消耗：19.8 MB, 在所有 Python3 提交中击败了5.05%的用户
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        def recur(node,pre):

            if node.next == None:
                node.next = pre
                return node
            temp = node.next
            node.next = pre
            pre = node
            return recur(temp, pre)
        c=recur(head,None)
        return c

b=gen_list([])
a=Solution().reverseList(b)
enum_node(a)