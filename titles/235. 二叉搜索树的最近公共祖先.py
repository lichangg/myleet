#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        if p.val>q.val:
            p,q=q,p

        while stack:
            node = stack.pop()
            if not node:
                continue
            if p.val<=node.val<=q.val:
                return node
            else:
                stack.append(node.left)
                stack.append(node.right)
