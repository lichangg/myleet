#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import TreeNode,create_BTree_By_List


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.count = 0
        self.node = None
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            self.count +=1
            if self.count == k:
                self.node = root
                return
            dfs(root.left)
        dfs(root)
        return self.node
b=create_BTree_By_List([3,1,4,None,2])
a=Solution().kthLargest(b,4)
print(a.val)
