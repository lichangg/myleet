#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import TreeNode, Tree


# 树的生成不好导致本地和线上不一致
class Solution:
    def rob(self, root: TreeNode) -> int:
        self.max_val = 0

        def dfs(root):
            if not root.val:
                return (0, 0)
            if not root.left and not root.right:
                return (0, root.val)
            tuple_l = dfs(root.left)
            tuple_r = dfs(root.right)
            need_son = max(tuple_l[1] + tuple_r[0], tuple_l[0] + tuple_r[1], tuple_l[1] + tuple_r[1])
            need_self = root.val + tuple_l[0] + tuple_r[0]
            self.max_val = max(need_son, need_self, self.max_val)
            return (need_son, need_self)

        self.max_val = max(dfs(root))
        return self.max_val


# 别人写的很优雅啊
class Solution:
    def rob(self, root: TreeNode) -> int:
        def _rob(root):
            if not root: return 0, 0  # 偷，不偷

            left = _rob(root.left)
            right = _rob(root.right)
            # 偷当前节点, 则左右子树都不能偷
            v1 = root.val + left[1] + right[1]
            # 不偷当前节点, 则对于子节点的成果不需要做限制,取最大的, 再左右相加
            v2 = max(left) + max(right)
            return v1, v2

        return max(_rob(root))


# 二刷,和上面完全一样
class Solution:
    def rob(self, root: TreeNode) -> int:
        def max_val(node):
            if not node: return 0, 0
            l = max_val(node.left)
            r = max_val(node.right)
            noneed_cur_val = max(l) + max(r)
            need_cur_val = l[0] + r[0] + node.val
            return noneed_cur_val, need_cur_val

        return max(max_val(root))


b = Tree()
[b.add(i) for i in [3, 2, 3, None, 3, None, 1]]
a = Solution().rob(b.root)
print(a)
