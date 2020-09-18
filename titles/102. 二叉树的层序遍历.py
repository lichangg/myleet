#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import Tree


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        l = root.left
        r = root.right
        stack = [l,r]
        res = [[root.val]]
        while stack and all(stack):
            nums = []
            for i in stack:
                if i.val:
                    nums.append(i.val)
            res.append(nums)
            temp = []
            for j in stack:
                if j:
                    temp.append(j.left)
                    temp.append(j.right)

            stack = temp

        return res

# 二刷,层序遍历
class Solution:

    def levelOrder(self, root) -> bool:
        res = []
        stack = [root]
        while stack:
            val_res = []
            temp = []
            for i in stack:
                if i:
                    val_res.append(i.val)
                    temp.append(i.left)
                    temp.append(i.right)

            stack = temp
            if val_res:
                res.append(val_res)
        return res

t=Tree()
[t.add(i)for i in [3,9,20,None,None,15,7]]
a=Solution().levelOrder(t.root)
print(a)