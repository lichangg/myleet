#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import TreeNode,create_BTree_By_List

# 我真是吐了,瞎几把写
# class Solution:
#     def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
#         def dfs(t1,t2,sub='l'):
#
#             if not t1 and not t2:
#                 return
#             if not t1 and t2:
#                 if sub == 'l':
#                     t1.left = TreeNode(t2.val)
#                     dfs(t1.left.left, t2.left, 'l')
#                     return
#                 else:
#                     t1.right = TreeNode(t2.val)
#                     dfs(t1.right.right, t2.right, 'r')
#                     return
#             if t1 and t2:
#                 t1.val = t1.val + t2.val
#             if not t2 and t1:
#                 if sub == 'l':
#                     t2.left = TreeNode(None)
#                     dfs(t1.left, t2.left.left, 'l')
#                     return
#                 else:
#                     t2.right = TreeNode(None)
#                     dfs(t1.right, t2.right.right, 'r')
#                     return
#
#             dfs(t1.left,t2.left, 'l')
#             dfs(t1.right,t2.right, 'r')
#         dfs(t1,t2)
#
#         return t1

# 我吐了,人家写的多优雅啊!!而且如果树的高度不一致, 直接就取了长的树,也不再递归下去了
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 or not t2:
            return t1 or t2
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left,t2.left)
        t1.right = self.mergeTrees(t1.right,t2.right)
        return t1