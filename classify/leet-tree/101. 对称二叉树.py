#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 思路1. 递归层次遍历暴力法
from utils.util_funcs import create_BTree_By_List
class Solution:

    def isSymmetric(self, root) -> bool:
        node_stack = [root]
        def valid(node_stack):
            if not any(node_stack):
                return
            val_stack = []
            for i in node_stack:
                if i:
                    val_stack.append(i.val)
                else:
                    val_stack.append(None)
            if val_stack[::-1] == val_stack:
                new_node_stack = []
                for i in node_stack:
                    if i:
                        new_node_stack.append(i.left)
                        new_node_stack.append(i.right)
                    else:
                        new_node_stack.append(None)
                        new_node_stack.append(None)

                return valid(new_node_stack)
            else:
                return 1

        return valid(node_stack) != 1
# 思路2. 迭代层次遍历暴力法 (不太明白这个比上面优化在了哪儿,反正时间少一个数量级)
class Solution:

    def isSymmetric(self, root) -> bool:
        def is_symmetric(nums):
            return nums == nums[::-1]
        stack = [root]
        while stack:
            res = []
            temp = []
            for i in stack:
                if i:
                    res.append(i.val)
                    temp.append(i.left)
                    temp.append(i.right)
                else:res.append(None)

            flag = is_symmetric(res)
            if not flag:
                return False
            stack = temp
        return True

b=create_BTree_By_List([1,2,2,None,3,None,3])
a=Solution().isSymmetric(b)
# print(a)
print(any([0,0,0]))