#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from utils.util_funcs import TreeNode

# 递归
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        def pre(node):
            if not node:
                return
            self.res.append(node.val)
            pre(node.left)
            pre(node.right)
        pre(root)
        return self.res

# 迭代
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        return res
