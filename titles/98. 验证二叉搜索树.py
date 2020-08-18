#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 本地和网站不一致.网站过不了[0]
class Solution:
    temp = float('-inf')
    FLAG=True
    def isValidBST(self, root) -> bool:
        def middle(node):
            if node:
                middle(node.left)
                if node.val > Solution.temp:
                    Solution.temp = node.val
                else:

                    Solution.FLAG = False
                middle(node.right)
        middle(root)
        return Solution.FLAG

