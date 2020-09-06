#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import ListNode, gen_list,enum_node
# 自己写的
# 执行用时：56 ms, 在所有 Python3 提交中击败了21.50%的用户
# 内存消耗：13.7 MB, 在所有 Python3 提交中击败了33.96%的用户
# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         if not l1 and not l2:
#             return None
#         if not (l1 and l2):
#             return l1 or l2
#         if l1.val > l2.val:
#             cur = l2
#             temp = l1
#         else:
#             cur = l1
#             temp = l2
#         head = cur
#         while cur.next:
#             if cur.next.val > temp.val:
#                 cur.next,temp = temp,cur.next
#             else:
#                 cur = cur.next
#         cur.next = temp
#         return head

# 别人的递归,看着很清爽
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2  # 终止条件，直到两个链表都空
        if not l2: return l1
        if l1.val <= l2.val:  # 递归调用
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2


#迭代的方式也挺简单的，
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 创建哑节点作为 结果链表 的开头
        dummy = ListNode(0)
        # 有个游标，标识 结果链表 的结尾
        move = dummy
        # l1 和 l2 都未遍历结束
        while l1 and l2:
            # 如果 l1 的数值比较小
            if l1.val <= l2.val:
                # 把 l1 头部节点拼接到 结果链表 的结尾
                move.next = l1
                # l1 指向下一个节点
                l1 = l1.next
            else:
                # 把 l2 头部节点拼接到 结果链表 的结尾
                move.next = l2
                # l2 指向下一个节点
                l2 = l2.next
            # 移动 结果链表 的结尾指针
            move = move.next
        # l1 或者 l2 尚未使用完，拼接到 结果链表 的最后
        move.next = l1 if l1 else l2
        # 返回哑节点的下一个位置
        return dummy.next



l1 = gen_list([])
l2 = gen_list([])
node=Solution().mergeTwoLists(l1,l2)
enum_node(node)