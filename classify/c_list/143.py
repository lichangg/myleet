#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import ListNode,gen_list,enum_node

# 思路1:
# 1. 遍历链表,存储所有节点和其对应的索引
# 2. 按规则重新赋值其next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        dic = {}
        cur = head
        idx= 0
        while cur:
            dic[idx] = cur
            cur = cur.next
            idx+=1

        max_idx = idx-1
        if idx<=2:
            return
        pre = None
        tmp, mod = divmod(idx,2)
        for i in range(tmp):
            if pre :
                dic[max_idx - i+1].next = dic[i]
            dic[i].next = dic[max_idx-i]
            pre = max_idx-idx
        # if mod == 1:
        #     dic[max_idx-i] = dic[tmp+1]
        if mod == 1:
            dic[max_idx-i].next = dic[tmp]
        dic[tmp].next = None

# 思路2:
# 1. 找到中间节点
# 2. 反转后半段
# 3. 将前半段一个插一个的合并


a=gen_list([1,2,3,4])
Solution().reorderList(head=a)
