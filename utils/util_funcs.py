#!/usr/bin/env python
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def gen_list(nums):
    if not nums:
        return None
    nodes = [ListNode(i) for i in nums]
    for index, i in enumerate(nodes):
        i.next = nodes[index + 1] if index < len(nodes) - 1 else None
    return nodes[0]

def enum_node(myhead:ListNode):
    while myhead:
        print(myhead.val)
        myhead = myhead.next