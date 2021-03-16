#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import TreeNode,create_BTree_By_List


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        stack = [root]
        while stack:
            tmp = []
            for i in stack:
                if i:
                    tmp.append(i.left)
                    tmp.append(i.right)
            i = 0
            l_tmp = len(tmp)
            while i < l_tmp:
                if tmp[i] == None:
                    i +=1
                else:
                    break
            j = l_tmp-1
            while j > 0:
                if tmp[j] == None:
                    j-=1
                else:
                    break
            for n in tmp[i:j+1]:
                if n.val == None:
                    return False
            stack = tmp
        return True
b=create_BTree_By_List([1,None, 2])
a=Solution().isCompleteTree(b)
print(a)