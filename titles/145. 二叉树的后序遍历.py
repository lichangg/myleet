#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

from utils.util_funcs import TreeNode


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        while stack:
            node = stack.pop()
            while