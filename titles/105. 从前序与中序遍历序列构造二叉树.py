#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import TreeNode, Tree
# 学到了
# 要明确一点是先序遍历(或后序遍历)和中序遍历出来的数组结果的索引实际上是有关联的
# 例如
# 先序[3,9,1,8,20,15,7]
# 中序[1,9,8,3,15,20,7]
# 也就是对于root 3 来说,通过中序遍历可以确定了它的左子树有多少个元素,然后再去先序遍历中往后推移这么多个元素就得到了左子树的先序遍历结果
class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        # preorder和inorder一定同时为空
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        root_index = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:root_index+1],inorder[:root_index])
        root.right = self.buildTree(preorder[root_index+1:],inorder[root_index+1:])
        return root
