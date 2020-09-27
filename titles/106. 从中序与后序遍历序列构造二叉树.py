#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 原理同上题
from typing import List

from utils.util_funcs import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        rootval = postorder[-1]
        rootindex = inorder.index(rootval)
        root = TreeNode(rootval)
        root.left = self.buildTree(inorder[:rootindex], postorder[:rootindex])
        root.right = self.buildTree(inorder[rootindex+1:], postorder[rootindex:-1])
        return root

inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
Solution().buildTree(inorder,postorder)