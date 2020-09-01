#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import TreeNode, create_BTree_By_List, Tree

#
# 执行用时：60 ms, 在所有 Python3 提交中击败了58.25的用户
# 内存消耗：15.9 MB, 在所有 Python3 提交中击败了52.04%的用户
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max = 0

        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            cur_max = l + r + 1
            self.max = max(self.max, cur_max)
            return max(l, r) +1

        dfs(root)
        return self.max - 1


b = Tree()

[b.add(i) for i in [1, 2, 3, 4, 5]]
a = Solution().diameterOfBinaryTree(b.root)
print(a)
