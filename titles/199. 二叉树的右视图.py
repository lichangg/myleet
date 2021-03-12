#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

from utils.util_funcs import TreeNode


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:return []
        res = []
        stack = [root]
        while stack:
            tmp = []
            res.append(stack[-1].val)
            for i in stack:
                if i.left:
                    tmp.append(i.left)
                if i.right:
                    tmp.append(i.right)
            stack = tmp
        return res
