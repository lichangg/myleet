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
            new_path = [i + root.val if root.val or root.val == 0 else 0 for i in path]
            self.count += new_path.count(self.sum)
            dfs(root.left, new_path[:])
            dfs(root.right, new_path[:])

        dfs(root, [])

        return self.count


# 再刷
# 构建到达每个节点所出现的所有可能的和的列表（含义为从根节点到目前节点为止的所有可能和），统计其中等于sum的个数
# 用这个数加上左右子节点返回上来的，加起来就是最终的结果
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def recur(node, sumlist):
            if not node: return 0
            sumlist = [i + node.val for i in sumlist] + [node.val]
            return sumlist.count(sum) + recur(node.left, sumlist) + recur(node.right, sumlist)

        return recur(root, [])



b = [1, 0, 1, 1, 2, 0, -1, 0, 1, -1, 0, -1, 0, 1, 0]
b = create_BTree_By_List(b)
a = Solution().pathSum(b, 2)
print(a)
