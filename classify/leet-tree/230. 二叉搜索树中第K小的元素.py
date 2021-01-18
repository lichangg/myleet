#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import TreeNode


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.count = 0
        self.res = None

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.count += 1
            if self.count == k:
                self.res = root.val
                return
            dfs(root.right)

        dfs(root)
        return self.res



