#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        self.res = False
        def dfs(node, s):
            if not node:
                return
            cur_sum = s - node.val
            if not node.left and not node.right and cur_sum == 0:
                self.res = True
                return
            dfs(node.left, cur_sum)
            dfs(node.right, cur_sum)
        dfs(root, targetSum)
        return self.res