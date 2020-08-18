#!/usr/bin/env python
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Tree(object):
    lt = []  # 依次存放左右孩子未满的节点

    def __init__(self):
        self.root = None

    def add(self, number):
        node = TreeNode(number)  # 将输入的数字节点化，使其具有左右孩子的属性
        if self.root == None:
            self.root = node
            Tree.lt.append(self.root)
        else:
            while True:
                point = Tree.lt[0] # 依次对左右孩子未满的节点分配孩子
                if point.left ==None:
                    point.left = node
                    Tree.lt.append(point.left)  # 该节点后面作为父节点也是未满的，也要加入到列表中。
                    return
                elif point.right ==None:
                    point.right = node
                    Tree.lt.append(point.right)  # 与左孩子同理
                    Tree.lt.pop(0)  # 表示该节点已拥有左右孩子，从未满列表中去除
                    return

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