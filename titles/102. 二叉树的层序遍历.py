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

t=Tree()
[t.add(i)for i in [3,9,20,None,None,15,7]]
a=Solution().levelOrder(t.root)
print(a)