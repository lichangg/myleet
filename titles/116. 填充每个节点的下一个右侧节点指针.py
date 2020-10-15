#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import TreeNode


class Solution:
    def connect(self, root: TreeNode) -> TreeNode:
        stack = [root]
        while stack[0]:
            temp = []
            n = 0
            while 0 < len(stack):
                temp.append(stack[n].left)
                temp.append(stack[n].right)
                if n == len(stack)-1:
                    stack[n].next = None
                    break
                stack[n].next = stack[n+1]
                n+=1

            stack = temp
        return root