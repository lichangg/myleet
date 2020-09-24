#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

from utils.util_funcs import TreeNode

# 用了额外的空间, 以后再看看没用额外空间的方法是怎样的吧
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.hashmap = {}
        def dfs(node):
            if node:
                self.hashmap[node.val] = self.hashmap.get(node.val, 0)+1
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        max_val = []
        max_freq = 0
        for i in self.hashmap:
            max_freq = max(max_freq,self.hashmap[i])

        for i in self.hashmap:
            if self.hashmap[i] == max_freq:
                max_val.append(i)

        return max_val