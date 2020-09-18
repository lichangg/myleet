#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

from utils.util_funcs import Tree, TreeNode
#这个简单
# 执行用时：60 ms, 在所有 Python3 提交中击败了41.98%的用户
# 内存消耗：19.5 MB, 在所有 Python3 提交中击败了5.06%的用户
class Solution:
    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        self.res = []
        if not root:
            return []
        def dfs(root, path):
            if not root:
                return

            path.append(root.val)
            cur_sum = sum(path)
            if cur_sum == s and not root.left and not root.right:
                self.res.append(path)
            dfs(root.left, path[:])
            dfs(root.right, path[:])
        dfs(root, [])
        return self.res

# 二刷优化一下,就是记录了一下当前和,不用每次都sum了,不过反倒慢了,看不懂
class Solution:
    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        self.res = []
        if not root:
            return []
        def dfs(root, path, cur_sum):
            if not root:
                return

            path.append(root.val)
            cur_sum+=root.val
            if cur_sum == s and not root.left and not root.right:
                self.res.append(path)
            dfs(root.left, path[:], cur_sum)
            dfs(root.right, path[:], cur_sum)
        dfs(root, [], 0)
        return self.res
b=Tree()
[b.add(i)for i in [0,1]]

a=Solution().pathSum(b.root,1)
print(a)