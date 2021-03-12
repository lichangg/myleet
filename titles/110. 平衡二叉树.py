#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Solution:
    def IsBalanced_Solution(self, pRoot):
        if not pRoot:return True
        def valid(node, level):
            if not node:
                return level
            l = valid(node.left, level+1)
            r = valid(node.right, level+1)
            if not l or not r:
                return
            if abs(l-r)<=1:
                return
            return max(l, r)
        return valid(pRoot, 1)
