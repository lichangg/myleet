#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import TreeNode
# 学到了, 在递归中还能返回需要的值....
# 关键思想: 既然是求最近的公共祖先A, 那么这两个点一定是在A的异侧!!!
# 采用dfs中的后序遍历, 遍历每一个节点, 若为空返回空且结束递归, 为pq之一则视为找到了其中一个节点(由于是后序遍历,最先找到的肯定是位于左侧的节点,不过这个不重要),
# 也结束递归并依次向上返回, 以示往上的父节点都包含这个left,
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 对于每一个可能的公共祖先节点来说, 有哪个节点就提供哪个节点,直到找到一个左右都有的根节点即最近的公共祖先节点
        if not right: return left
        if not left: return right
        return root

