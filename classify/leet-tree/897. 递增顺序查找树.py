#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import TreeNode

# yeild from不返回空值,只返回下一个非空值
class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        ans = cur = TreeNode(None)
        for v in inorder(root):
            cur.right = TreeNode(v)
            cur = cur.right
        return ans.right
