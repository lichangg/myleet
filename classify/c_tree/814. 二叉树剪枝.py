#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import TreeNode


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root:
                return
            else:
                l_flag = dfs(root.left)
                if not l_flag:
                    root.left = None
                r_flag = dfs(root.right)
                if not r_flag:
                    root.right = None
                if any([l_flag,r_flag, root.val]):
                    return 1
                else:
                    return

        flag = dfs(root)
        if not flag and root.val == 0:return

        return root

class Solution(object):
    def pruneTree(self, root):
        def containsOne(node):
            if not node: return False
            a1 = containsOne(node.left)
            a2 = containsOne(node.right)
            if not a1: node.left = None
            if not a2: node.right = None
            return node.val == 1 or a1 or a2

        return root if containsOne(root) else None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root or (root.val == 0 and not root.left and not root.right):
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val == 0 and not root.left and not root.right:
            return None
        return root