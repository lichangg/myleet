#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

from utils.util_funcs import TreeNode, TreeCreator

# 思路: 先建立对父节点的联系,之后再dfs还是bfs就随便了
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:

        dfs(root, target, 0)
b=TreeCreator().deserialize([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
