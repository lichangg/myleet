#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import TreeNode,create_BTree_By_List



# 别人的思路很好
# 除根节点外，每一个节点都是父节点的子节点，所以：
# 1、根节点没有父节点，要考虑自己
# 2、非根节点只考虑子节点即可，因为自己会被作为父节点的子节点被考虑到
#
# 把节点值当作节点状态：
# 0：没拍别人也没被拍，需要被人拍
# 1：被拍了
# 2：拍别人

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:

        self.res = 0

        def lrd(node):
            if node is None:
                return 1  # 空节点不需要被人拍也不用拍别人，直接返回被拍了就好
            left = lrd(node.left)
            right = lrd(node.right)
            if left == 0 or right == 0:
                # 如果左儿子或者右儿子需要被拍，我就装个摄像机
                self.res += 1
                return 2
            if left == 2 or right == 2:
                # 如果左儿子或者右儿子装了摄像机，那我就被拍了
                return 1
            else:  # left == 1 and right == 1:
                # 如果左儿子和右儿子都是被拍的，都没有摄像机，那我就是需要被拍的状态
                return 0

        if lrd(root) == 0:
            ##看看根节点是不是需要被拍
            self.res += 1
        return self.res



a=create_BTree_By_List([0,0,None,0,None,0,None,None,0])
Solution().minCameraCover(a)
a.preorder()