#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import TreeNode,create_BTree_By_List
# 学到了
# 从根节点开始的操作
# 1.如果没有左节点
#   情形1: 如果有右节点,右节点成为根继续递归
#   情形2: 如果没有右节点,直接返回
# 2.如果有左节点: 找到其最右的叶子节点A(此节点不在某个右分支而在左分支也没关系的,只要保证他是处在最右的位置就行)
#   1. 该左节点的右分支给A
#   2. 该左节点左分支给右分支
#   3. 该左节点左分支置空
# 执行用时：40 ms, 在所有 Python3 提交中击败了97.25%的用户
# 内存消耗：14.6 MB, 在所有 Python3 提交中击败了46.93%的用户
class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        if not root.left:
            if root.right:
                self.flatten(root.right)
            else:
                return
        else:
            cur = root.left
            while cur.right or cur.left:
                if cur.right:
                    cur=cur.right
                else:
                    cur = cur.left
            cur.right = root.right
            root.right = root.left
            root.left = None
            self.flatten(root.right)


class Solution:
    def flatten(self, root: TreeNode) -> None:
        cur = root
        while cur:
            r = cur.right
            l = cur.left
            if l:
                l_node = l
                while l_node and (l_node.right or l_node.left):
                    l_node = l_node.right or l_node.left

                l_node.right = r
                cur.right = l
            # 要注意左边要置为None. 不然翻车了
            cur.left=None
            cur = cur.right

b=create_BTree_By_List([])
Solution().flatten(b)
b.preorder()