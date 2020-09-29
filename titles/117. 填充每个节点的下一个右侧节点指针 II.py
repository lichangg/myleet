#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import create_BTree_By_List
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # 层级遍历
        # 深度优先搜索
        if not root:
            return root
        # 神奇,这里我改成双端队列后竟然慢了一点
        stack = deque()
        stack.append((root, 0))

        stack = [(root, 0)]
        while True:
            node, level = stack.popleft()
            # node, level = stack.pop(0)
            if node.left:
                stack.append((node.left, level+1))
            if node.right:
                stack.append((node.right, level+1))
            if not stack:
                break
            if level == stack[0][1]:
                node.next = stack[0][0]
        return root



b=create_BTree_By_List([1,2,3])
a=Solution().connect(b)
