#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 初始化失败
# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         dps = [[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]
#         n1 = len(word1)
#         n2 = len(word2)
#         for j in range(1, n2 + 1):
#             dps[0][j] = dps[0][j-1] + 1
#         # 第一列
#         for i in range(1, n1 + 1):
#             dps[i][0] = dps[i-1][0] + 1
#
#
#         rows, cols = len(word2), len(word1)
#         r = 1
#         while r < rows+1:
#             c = 1
#             while c < cols+1:
#                 if word1[c] == word2[r]:
#                     dps[r][c] = min(dps[r - 1][c], dps[r][c - 1], dps[r - 1][c - 1])
#                 else:
#                     dps[r][c] = min(dps[r - 1][c], dps[r][c - 1], dps[r - 1][c - 1]) + 1
#                 c+=1
#             r+=1
#         return dps[-1][-1]

# 前面加个"",初始化直接美好了起来
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        # 第一行
        for j in range(1, n2 + 1):
            dp[0][j] = dp[0][j-1] + 1
        # 第一列
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i-1][0] + 1
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1] ) + 1
        #print(dp)
        return dp[-1][-1]



a = Solution().minDistance(word1 = "horse", word2 = "ros")
print(a)
