#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

from utils.util_funcs import TreeNode, create_BTree_By_List

# 思路: 先建立对父节点的联系,之后再dfs还是bfs就随便了
# 这样搞会导致力扣反序列化有问题
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        self.visited = set()
        self.res = []

        def dfs(node, father):
            if not node:
                return
            node.father = father
            dfs(node.left, node)
            dfs(node.right, node)

        def dfs2(node, dis):
            if not node or node in self.visited:
                return
            dis +=1
            self.visited.add(node)

            if dis == K:
                print(node)
                self.res.append(node)
                return
            else:
                dfs2(node.left, dis)
                dfs2(node.right, dis)
                dfs2(node.father, dis)
        dfs(root, None)
        dfs2(target, -1)
        return self.res


b=create_BTree_By_List([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
a=Solution().distanceK(b, TreeNode(5), 2)
