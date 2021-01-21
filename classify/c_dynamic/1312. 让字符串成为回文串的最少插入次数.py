#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 这种思路还是不对, 解决不了源字符串中心是偏向两边的情况,可能可以通过枚举字符串中心解决
# class Solution:
#     def minInsertions(self, s: str) -> int:
#         head = 0
#         tail = len(s) - 1
#         count = 0
#         while head < tail:
#             if s[head] == s[tail]:
#                 head += 1
#                 tail -= 1
#             else:
#                 if s[head + 1] == s[tail]:
#                     head += 1
#                     count += 1
#                 elif s[head] == s[tail - 1]:
#                     tail -= 1
#                     count += 1
#                 else:
#                     count += 2
#                     head += 1
#                     tail -= 1
#         return count

# 动态规划
# 定义dp[i][j]为区间s[i:j](包含索引为i,j的字符)成为回文串的最少插入字符数
#   - 若s[i] == s[j]说明最外层已经是回文了, 只要用里面的回文状态转移出来就行,也就是dp[i][j] = dp[i+1][j-1]
#   - 若s[i] != s[j]说明最外层不是回文,这时候可以从这两个状态转移出来, 一个是dp[i+1][j],一个是dp[i][j-1], 取两者中较小的再+1就行
# 还要解决的问题是初始的s[i:j]怎么取, 这里需要遍历枚举, 代码中span为子区间长度, 由span得到j, 也就是把所有的i, j可以取到的值都取到, 不断更新dp数组
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for span in range(2, n + 1):
            for i in range(n - span + 1):
                j = i + span - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
        return dp[0][n - 1]
# 递归也太香了吧
class Solution:
    def minInsertions(self, s: str) -> int:
        memo = dict()
        def dp(i, j):
            # s[i,j]最少插入多少字符成为回文
            if (i, j) in memo:return memo[(i,j)]
            if i >= j: return 0
            if s[i] == s[j]:
                memo[(i,j)] = dp(i+1, j-1)
            else:
                memo[(i,j)] = min(dp(i+1,j), dp(i,j-1))+1
            return memo[(i, j)]
        return dp(0, len(s) - 1)
# 可转化为倒序字符串和原字符串的最长公共子序列的长度x, 再用原字符串长度减去x就行, 暂时没有明白为什么可以这样
class Solution:
    def minInsertions(self, s: str) -> int:
        s1 = s[::-1]
        return len(s1) - self.longestCommonSubsequence(s,s1)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2: return 0
        len1 = len(text1)
        len2 = len(text2)
        dp = [[0] * len1 for _ in range(len2)]
        i = 0
        while i < len2:
            j = 0
            while j < len1:
                if i == 0 and j == 0:
                    dp[i][j] = 1 if text1[0] == text2[0] else 0
                elif i == 0 and j > 0:
                    dp[i][j] = dp[i][j-1]
                    if text1[j] == text2[i]:
                        dp[i][j]=1
                elif j==0 and i>0:
                    dp[i][j] = dp[i-1][j]
                    if text1[j] == text2[i]:
                        dp[i][j]=1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    if text1[j] == text2[i]:
                        dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)
                j += 1
            i += 1

        return dp[-1][-1]
a = Solution().minInsertions('leetcode')
print(a)
