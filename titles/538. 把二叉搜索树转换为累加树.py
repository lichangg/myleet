#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Definition for a binary tree node.
# 该题和1038题相同
from utils.util_funcs import TreeNode

# 我吐了 ,递归思路就是用一个cur保存当前列加的和, 遍历顺序是右中左就行了
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        cur = 0

        def dfs(root):
            nonlocal cur
            if not root: return
            dfs(root.right)
            cur += root.val
            root.val = cur
            dfs(root.left)

        dfs(root)
        return root


#思路同上,但是写法不一样,一个是递归一个是while, 学到了,好好看看
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        cur, stack, p = 0, [], root
        while p or stack:
            while p:
                stack.append(p)
                p = p.right
            p = stack.pop()
            cur += p.val
            p.val = cur
            p = p.left
        return root


