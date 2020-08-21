#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 学到了
# 每个节点可以推得一个重要属性:该节点能够贡献的最大值
# 而以该节点为根的最大路径和由 [左节点的最大贡献值(为正才计入) + 右节点的最大贡献值(为正才计入) + 该节点的值] 得到
from utils.util_funcs import TreeNode, Tree


class Solution:
    ans = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        def helper(node):
            if not node or not node.val: return 0
            l = helper(node.left)
            r = helper(node.right)
            # 此处计算的是以该节点为根的最大路径和
            self.ans = max(self.ans, max(l, 0) + max(r, 0) + node.val)
            # 此处返回的是该节点能够贡献的最大值
            return max(l, r, 0) + node.val

        helper(root)
        return self.ans


t = Tree()
[t.add(i) for i in [-10, 9, 20, None, None, 15, 7]]
a = Solution().maxPathSum(t.root)
print(a)
