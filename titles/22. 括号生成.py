#!/usr/bin/env python
# -*- coding:utf-8 -*-
#一颗剪了枝的二叉树, 另外核心判断点:是右括号加入的时机,它始终不会比左括号多
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.dfs(res, n, n, '')
        return res

    def dfs(self, res, left, right, path):
        if left == 0 and right == 0:
            res.append(path)
            return
        if left > 0:
            self.dfs(res, left - 1, right, path + '(')
        # 此处判断是因为当左次数更少时也就是左括号更多时,这才能继续往下搜
        if left < right:
            self.dfs(res, left, right - 1, path + ')')


a=Solution().generateParenthesis(3)