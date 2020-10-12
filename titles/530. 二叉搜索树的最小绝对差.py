# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from utils.util_funcs import TreeNode


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.min = float('inf')
        l = []
        def middle_order(node):
            if not node:
                return
            middle_order(node.left)
            l.append(node.val)
            middle_order(node.right)
        middle_order(root)
        i=0
        while i<len(l)-1:
            self.min = min(self.min, abs(l[i]-l[i+1]))
            i+=1
        return self.min


# 别人的解答
# 维护一个前驱节点pre, 这样就不用像上面那样还得存所有元素然后遍历一遍了, 不过奇怪的是这样反而慢了一点点
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        # 定义变量 ans 存储最小值，初始化为 float('inf')
        self.ans = float('inf')
        # pre 记录前驱节点
        self.pre = -1
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            # 节点值处理，
            if self.pre != -1:
                # 比较相邻元素差值，取最小值
                self.ans = min(self.ans, root.val - self.pre)
            # 维护更新 pre
            self.pre = root.val
            dfs(root.right)
        dfs(root)

        return self.ans

