#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 一颗剪了枝的二叉树, 另外核心判断点:是右括号加入的时机,它始终不会比左括号多,(深度优先搜索,二叉树),这个貌似没有回溯操作
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

# 二刷时自己写的，这里有个判断啥时候退出的逻辑l_count>self.n，，感觉不够优雅，上面那个算法是倒着来的，感觉好一些
class Solution(object):
    def generateParenthesis(self, n):
        self.res = []
        self.n = n
        def dfs(path, add):
            curpath = path + add
            l_count = curpath.count('(')
            r_count = curpath.count(')')
            if l_count < r_count or l_count>self.n:
                return
            elif l_count == r_count ==self.n:
                self.res.append(curpath)
                dfs(curpath, '(')
            else:
                dfs(curpath, '(')
                dfs(curpath, ')')

        dfs('', '(')
        return self.res

# 再刷, 思路异常清晰, 牛逼
class Solution(object):
    def generateParenthesis(self, n):
        self.res = []
        def dfs(s, cur, l_count, r_count):
            if l_count < r_count or l_count > n:
                return
            new_s = s + cur
            if l_count == r_count == n:
                self.res.append(new_s)
                return
            dfs(new_s, '(', l_count+1, r_count)
            dfs(new_s, ')', l_count, r_count+1)
        dfs('', '(', 1, 0)
        return self.res
a = Solution().generateParenthesis(3)
print(a)
