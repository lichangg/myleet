#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.right, root.left = root.left,root.right
            self.invertTree(root.left)
            self.invertTree(root.right)

            return root
