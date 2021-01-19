#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import ListNode,gen_list

def func(l, node, k):
    pre = None
    while node:
        node.pre = pre
        pre = node
        node = node.next
    count = 0
    while count < k or not pre:
        pre = pre.pre
        count+=1
    if not pre:return None
    return pre.next.val

b=gen_list([1, 2, 3, 4, 5, 6, 7, 8])
print(func(8,b,1))