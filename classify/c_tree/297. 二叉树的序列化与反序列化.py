#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

from utils.util_funcs import TreeNode, create_BTree_By_List
# class Codec:
#     def serialize(self, root):
#         """Encodes a tree to a single string.
#
#         :type root: TreeNode
#         :rtype: str
#         """
#         if not root:
#             return '[]'
#         self.li = '['
#         def dfs(node):
#             if not node:
#                 self.li += 'null,'
#                 return
#             else:
#                 self.li +=str(node.val)+','
#                 dfs(node.left)
#                 dfs(node.right)
#         dfs(root)
#         self.li = self.li.rstrip(',')
#         self.li +=']'
#         return self.li
#
#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
#
#         :type data: str
#         :rtype: TreeNode
#         """
#         li = json.loads(data)
#         stack = [TreeNode(li.pop(0))]
#         while li:
#             node = stack.pop(0)
#             if li:
#                 node.left = TreeNode(li.pop(0))
#                 stack.append(node.left)
#
#             if li:
#                 node.right = TreeNode(li.pop(0))
#                 stack.append(node.right)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # 解法1 层序遍历方式
        if not root: return ''

        from collections import deque
        q = deque([root])
        ans = []
        while q:
            node = q.popleft()
            ans.append(str(node.val) if node else '#')
            if node: q.extend([node.left, node.right])
        return ','.join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data: return

        nodes = [(TreeNode(int(v)) if v != '#' else None) for v in  data.split(',')]
        i, j = 0, 1
        while j < len(nodes):
            if nodes[i] is not None:
                nodes[i].left = nodes[j]
                j += 1
                nodes[i].right = nodes[j]
                j += 1
            i += 1
        return nodes[0]


b=create_BTree_By_List([1,2,3,4,5])
a=Codec().serialize(b)
print(a)
c=' s dfas '
print(c.strip())