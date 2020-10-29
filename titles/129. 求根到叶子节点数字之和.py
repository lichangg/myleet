#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from utils.util_funcs import TreeNode


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.res = 0
        if not root:
            return 0

        def postorder(node, path):
            cur_path = path * 10 + node.val
            if node.left:
                postorder(node.left, cur_path)
            if node.right:
                postorder(node.right, cur_path)
            if not node.left and not node.right:
                self.res += cur_path

        postorder(root, 0)
        return self.res




