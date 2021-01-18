#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils.util_funcs import TreeNode,create_BTree_By_List

# 虽然用深度遍历过了,但是实在不优雅
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.col_parent = None
        def dfs(node, p, q):
            flag = 0
            if not node:
                return flag

            if node.val == p.val or node.val == q.val:
                flag = 1
            res1 = dfs(node.left, p, q)
            res2 = dfs(node.right, p, q)
            if flag+res1+res2 == 2:
                self.col_parent = node
                return 0
            return res1 or res2 or flag
        dfs(root, p,q)
        return self.col_parent
# 优雅一点
# 很精髓的一个思想就是,
# 对于当前root, 没有右就返回左, 没有左就返回右,
# 有右有左的意思就是p, q分别在root的左右子树, 然后将当前root(该root已经凑齐p, q), 然后返回至上一级节点pre_root,
#   - root是pre_root的左节点, 右节点必然返回空值
#   - root是pre_root的右节点, 左节点必然返回空值
# 凑齐的该root层层往上返回, 最后就返回出来了
# 另外对于公共祖先是其中之一的情况.例如[3,5,1,6,2]找5,2, 程序中左树深度遍历到5就不会往下了, 你可能会有疑问: 5下面要是有另一个数2那不是找不到了?
# 其实没关系, 因为右子树必然是层层返回空的, 所以对于root节点3来说,左一已经有5了, 右也必然返回空值, 按照没右返左, 没左返右就出来了
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root.val == p.val or root.val == q.val: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 对于每一个可能的公共祖先节点来说, 有哪个节点就提供哪个节点,直到找到一个左右都有的根节点即最近的公共祖先节点
        if not right: return left
        if not left: return right
        return root


b=create_BTree_By_List([3,5,1,6,2])
a=Solution().lowestCommonAncestor(b,TreeNode(5),TreeNode(2))
print(a.val)
