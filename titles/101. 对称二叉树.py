#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import Tree
# 这个测试用例[1,2,2,None,3,None,3]过不了,本地能过
#
class Solution:
    FLAG=True
    def isSymmetric(self, root) -> bool:
        l = root.left
        r = root.right
        stack = [l,r]
        while stack and all(stack):
            nums = []
            for i in stack:
                nums.append(i.val)
            mid=int(len(nums)/2)
            if nums[:mid]!=nums[mid:][::-1]:
                Solution.FLAG = False
                break
            temp = []
            for j in stack:
                if j:
                    temp.append(j.left)
                    temp.append(j.right)

            stack = temp

        return Solution.FLAG
t=Tree()
[t.add(i)for i in [1,2,2,None,3,None,3]]
a=Solution().isSymmetric(t.root)
print(a)