#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import TreeNode

# 思路1.递归
# 1. 递归函数参数的含义:
#   - node: 当前节点
#   - count: 到当前几点前累计的路径长度
#   - pre_direc: 通过何种方向到达的该node节点('l'为走左路到达, 'r'为走右路到达)
# 2. 初始分别给左右两个方向, 递归函数中若满足交错则count进行累计, 若不满足交错则count归0重来

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if not root or (not root.left and not root.right):return 0
        self.max_step = 0
        def dfs(node, count, pre_direc):
            if not node:
                return
            count += 1
            self.max_step = max(self.max_step, count)

            if pre_direc == 'r':
                dfs(node.left, count, 'l')
                dfs(node.right, 0, 'r')

            if pre_direc == 'l':
                dfs(node.right, count, 'r')
                dfs(node.left, 0, 'l')

        dfs(root.left, 0, 'l')
        dfs(root.right, 0, 'r')
        return self.max_step