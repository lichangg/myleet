#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

from utils.util_funcs import TreeNode,create_BTree_By_List


class Solution:
    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        self.res = []

        def dfs(node, diff, path):

            if not node:
                return
            new_path  = path[:]
            new_path.append(node.val)
            diff = diff - node.val
            if diff == 0 and not node.left and not node.right:
                self.res.append(new_path)
                return
            dfs(node.left, diff, new_path)
            dfs(node.right, diff, new_path)

        dfs(root, s, [])
        return self.res

b=create_BTree_By_List([5,4,8,11,None,13,4,7,2,None,None,5,1])
a=Solution().pathSum(b,22)
print(a)