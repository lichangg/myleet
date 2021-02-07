#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

from utils.util_funcs import TreeNode, create_BTree_By_List


# 递归,不够优雅
class Solution:
    def inorderTraversal(self, root):
        res = []
        if not root:
            return []
        def middle(node):
            if node:
                middle(node.left)
                res.append(node.val)
                middle(node.right)
        middle(root)
        return res
# 优雅的递归
class Solution:
    def inorderTraversal(self, root: TreeNode):
        if not root:
            return []
        # 前序递归
        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        # # 中序递归
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        # # 后序递归
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

# 迭代方法1
class Solution:
    def inorderTraversal(self, root: TreeNode):
        res = []
        stack = []
        cur = root
        # 中序，模板：先用指针找到每颗子树的最左下角，然后进行进出栈操作
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            # 循环至没有节点再从stack中取
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res

        # # 前序，相同模板
        # while stack or cur:
        #     while cur:
        #         res.append(cur.val)
        #         stack.append(cur)
        #         cur = cur.left
        #     cur = stack.pop()
        #     cur = cur.right
        # return res

        # # 后序，相同模板,不同之处在于res顺序是:根右左, 然后取[::-1]就行了, 学到了
        # while stack or cur:
        #     while cur:
        #         res.append(cur.val)
        #         stack.append(cur)
        #         cur = cur.right
        #     cur = stack.pop()
        #     cur = cur.left
        # return res[::-1]

# 迭代2 该模板貌似没法中序
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        # # 前序迭代模板：最常用的二叉树DFS迭代遍历模板
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res

        # # 后序迭代，相同模板：将前序迭代进栈顺序稍作修改，最后得到的结果反转
        # while stack:
        #     cur = stack.pop()
        #     if cur.left:
        #         stack.append(cur.left)
        #     if cur.right:
        #         stack.append(cur.right)
        #     res.append(cur.val)
        # return res[::-1]

# 三色标记法, 厉害,白色表示未访问过的节点, 灰色表示未访问完全的节点, 黑色表示已完全访问了的节点(不过这里用不到),
# 用类似递归的写法来写迭代, 更好记忆一些
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                # 中序
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
                # 前序
                # stack.append((GRAY, node))
                # stack.append((WHITE, node.right))
                # stack.append((WHITE, node.left))
                # 后序
                # stack.append((WHITE, node.right))
                # stack.append((GRAY, node))
                # stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res

# 再写一次迭代, 我吐了,写得太不优雅了
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:return
        node = root
        stack = [node]
        res = []
        while stack or node:
            while node:
                node = node.left
                if node:
                    stack.append(node)
            node = stack.pop()
            res.append(node.val)
            node = node.right
            if node:
                stack.append(node)
        return res

# 再来一次二叉树的中序遍历
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        node = root
        res = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res


b=create_BTree_By_List([1])
a=Solution().inorderTraversal(b)
print(a)