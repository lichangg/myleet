#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Definition for a binary tree node.
from utils.util_funcs import TreeNode, create_BTree_By_List

# 算出每个节点能够得到的可能的值
# 执行用时：320 ms, 在所有 Python3 提交中击败了55.36%的用户
# 内存消耗：39.3 MB, 在所有 Python3 提交中击败了5.05%的用户
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.sum = sum
        self.count = 0

        def dfs(root, path):
            if not root:
                return
            path.append(0)
            new_path = [i + root.val if root.val or root.val == 0 else 0 for i in path ]
            self.count += new_path.count(self.sum)
            dfs(root.left, new_path[:])
            dfs(root.right, new_path[:])

        dfs(root, [])

        return self.count
b = [1,0,1,1,2,0,-1,0,1,-1,0,-1,0,1,0]
b = create_BTree_By_List(b)
a = Solution().pathSum(b, 2)
print(a)
