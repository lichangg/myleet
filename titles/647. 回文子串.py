#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 注意, 若采用dp的话不知道怎么dp

# 直接深度遍历+剪枝, 但是好像复杂度很高
# 执行用时：1064 ms, 在所有 Python3 提交中击败了5.04%的用户
# 内存消耗：15.2 MB, 在所有 Python3 提交中击败了36.35%的用户
class Solution:

    def countSubstrings(self, s: str) -> int:
        self.count = 0

        def dfs(begin, s, path):
            if begin >= len(s):
                return
            curpath = path + s[begin]
            if len(curpath) == 1 or curpath == curpath[::-1]:
                self.count += 1
            dfs(begin + 1, s, curpath)

        for index, i in enumerate(s):
            dfs(index, s, '')
        return self.count


# 中心扩展法,这个时间是O(N**2),空间是O(1),厉害多了
# 思路是从中心点往两边扩散, 所有的单个字符和所有的连续双字符都是中心点

# 执行用时：168 ms, 在所有 Python3 提交中击败了65.57%的用户
# 内存消耗：13.5 MB, 在所有 Python3 提交中击败了95.79%的用户
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        self.res = 0

        def helper(i, j):
            # 扩散操作一旦有扩散的左右两字符串不一致的情况就立即终止
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
                self.res += 1

        for i in range(n):
            # 从中心点是单字符的出发开始向相变扩散找
            helper(i, i)
            # 从中心点是双字符的出发开始向两边扩散找
            helper(i, i + 1)
        return self.res


# 再刷
# 这种方式执行用时在2000ms,内存180MB,太不好了,虽然它很好理解
# 核心思想在于 i到j的回文字串数等于 和i,j都完全无关的数量 +        和i无关的数量        +      和j无关的数量
#                   dfs(i, j) = dfs(i+1, j-1)   + [dfs(i, j) - dfs(i, j-1)] + [dfs(i,j)-dfs(i+1, j)]
class Solution:
    def countSubstrings(self, s: str) -> int:
        self.cache = {}

        def dfs(i, j):
            if i > j :
                return 0
            if (i, j) in self.cache:
                return self.cache[(i, j)]
            if j == i:
                return 1

            res = dfs(i, j - 1) + dfs(i + 1, j) - dfs(i + 1, j - 1)
            if s[i:j+1] == s[i:j+1][::-1]:
                res +=1
            self.cache[(i, j)] = res
            return res

        return dfs(0, len(s)-1)

# 动态规划
# 设dp[i][j]表示s[i:j+1]是否为回文子串
# 转移方程:如果dp[i+1:.j-1]回文且s[i]==s[j]: 那么dp[i][j] = 1
#   a b a d c
# a 1 0 1 0 0
# b 0 1 0 0 0
# a 0 0 1 0 0
# d 0 0 0 1 0
# c 0 0 0 0 1
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        # dp = [[1 if x == y else 0 for y in range(n)] for x in range(n)]
        dp = [[0] * n for _ in range(n)]
        self.count = 0
        # 斜着进行状态转移
        for span in range(1,n+1):
            for i in range(n-span+1):
                j = span+i-1
                if i == j:
                    dp[i][j] =1
                elif s[i] == s[j]:
                    if j-1 == i:
                        dp[i][j] =1
                    else:
                        dp[i][j] = dp[i+1][j-1]

                if dp[i][j] == 1:
                    self.count+=1
        return self.count

a = Solution().countSubstrings('aaaa')
print(a)
