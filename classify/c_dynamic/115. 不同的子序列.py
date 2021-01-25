#!/usr/bin/env python
# -*- coding:utf-8 -*-
# dfs直接超时,下面这个用例超时, 超时原因不解释了
# "bdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"
# "bddabdcae"
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        self.count = 0

        def dfs(idx, char, path):
            path += char
            l = len(path)
            if path != t[:l]:
                return
            if path == t:
                self.count += 1
                return
            if path in self.cache:

            for new_idx, new_i in enumerate(s):
                if new_idx <= idx:
                    continue
                else:
                    dfs(new_idx, new_i, path)

        for idx, i in enumerate(s):
            dfs(idx, i, '')
        return self.count

# 动态规划
# 这里面很难想的就是转移方程:
#    '' r a b b b i t
# '' 1 1 1 1 1 1 1 1
# r  0 1 1 1 1 1 1 1
# a  0 0 1 1 1 1 1 1
# b  0 0 0 1 2 3 3 3
# b  0 0 0 0 1 3 3 3
# i  0 0 0 0 0 0 3 3
# t  0 0 0 0 0 0 0 3
# 当s[i] != t[j] 的时候, 好说, dp[j][i] = dp[j][i-1]
# 当s[i] == t[j] 的时候, dp[j][i] = dp[j][i-1] + dp[j-1][i-1]
# 解释当s[i] == t[j] 的时候:
# 1. dp[j][i-1]的意思是s不要最后一个字符串, 看有多少种匹配法
# 2. dp[j-1][i-1]的意思是在s和t都不要最后一个串的时候, 有多少种匹配法
# 现在dp[i][j]既然是s要最后一个字符串, 那自然就是[1]和[2]相加
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
a = Solution().numDistinct("bdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"
,"bddabdcae")
print(a)