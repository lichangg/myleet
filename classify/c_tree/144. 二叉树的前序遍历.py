#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

from utils.util_funcs import TreeNode,create_BTree_By_List

# 迭代, 线性时间和空间
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        node = root
        stack = []
        res = []
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return res

# morris遍历, 线性时间和常数空间
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = list()
        if not root:
            return res

        p1 = root
        while p1:
            p2 = p1.left
            if p2:
                while p2.right and p2.right != p1:
                    p2 = p2.right
                if not p2.right:
                    res.append(p1.val)
                    p2.right = p1
                    p1 = p1.left
                    continue
                else:
                    p2.right = None
            else:
                res.append(p1.val)
            p1 = p1.right

        return res

b=create_BTree_By_List([1,2,3,4,5,6,7])
a=Solution().preorderTraversal(b)
print(a)