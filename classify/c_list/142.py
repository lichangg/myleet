#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import ListNode

# 思路1:用dict存走过的节点, 第一个重复的节点就是入环的节点
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        dic = {}
        index =0
        cur = head
        while cur:
            if cur not in dic:
                dic[cur] = index
            else:
                return cur
            cur = cur.next

        return None

# 思路二
# 采用快慢双指针. 设链表总长度为 a + b ,a指从开头到环入口(不包含环入口,) b是环的长度, 经过分析可以得到
# 推理1. 走到环入口需要 a+nb 步, n指慢指针在环内走过的圈数,
# 推理2. 快慢指针同时走, 快指针走过的步数f等于两倍慢指针的步数s, 也就是 f=2s[这个是恒成立的][1] 当第一次相遇时, 还会有一个结论是f=s+nb[意思就是重合时快指针比慢多走nb步][2]
# 由式子1和2可得当第一次相遇时s=nb, 也就是慢指针走了nb步
# 再由 推理1得到此时慢指针再走a步就到入口点, 问题是不知道a是多少, 由a的定义可以知道从头到入口点是a步,所以再构造一个从头节点出发的指针, 它和慢指针同时一直往下走
# 当他们相遇时,此时的节点就是环入口节点[此时新指针走了a, 慢指针走了a+nb]
# class Solution:
#     def detectCycle(self, head: ListNode) -> ListNode:
