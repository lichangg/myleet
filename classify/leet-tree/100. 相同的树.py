#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import TreeNode

# 递归退出条件是q先为None或者p先为None或者两个值不相等, 此时往外发送信号
# 若递归完了都没有接收到信号则表明全部节点值相等
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not q and not p: return True

        def eq(p, q):
            if not q and not p:
                return
            if (q and not p) or (p and not q) or q.val != p.val:
                return 1
            return eq(p.left, q.left) or eq(p.right, q.right)

        return eq(p, q) != 1



