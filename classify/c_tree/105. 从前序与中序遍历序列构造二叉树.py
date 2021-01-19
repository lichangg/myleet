#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 思路1. 递归
from utils.util_funcs import TreeNode
class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if not preorder:
            return None
        rootval = preorder[0]
        root = TreeNode(rootval)
        root_idx = inorder.index(rootval)
        root.left = self.buildTree(preorder[1:root_idx+1], inorder[0:root_idx])
        root.right = self.buildTree(preorder[root_idx+1:], inorder[root_idx+1:])
        return root
a=Solution().buildTree(preorder = [3,9,20,15,7],
inorder = [9,3,15,20,7])
print(a)

