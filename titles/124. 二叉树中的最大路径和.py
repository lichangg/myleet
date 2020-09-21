#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 学到了
# 每个节点可以推得一个重要属性:该节点能够贡献的最大值
# 而以该节点为根的最大路径和由 [左节点的最大贡献值(为正才计入) + 右节点的最大贡献值(为正才计入) + 该节点的值] 得到
from utils.util_funcs import TreeNode, Tree,create_BTree_By_List


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


class Solution:

    def maxPathSum(self, root: TreeNode) -> int:
        self.max = float('-inf')

        def dfs(cur_node):
            # 这里一定不要用not 来判断,而要用==None判断, 防止该节点值是0的情况
            if cur_node == None or cur_node.val == None:
                return 0
            l_max = max(0, dfs(cur_node.left))
            r_max = max(0, dfs(cur_node.right))
            cur_max = cur_node.val + l_max + r_max
            self.max = max(cur_max, self.max)
            max_from_sub = cur_node.val + max(l_max, r_max)
            return max_from_sub

        dfs(root)
        return self.max


b=create_BTree_By_List([0,1,1])
a = Solution().maxPathSum(b)
print(a)
