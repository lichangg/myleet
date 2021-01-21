#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Solution:
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


a = Solution().longestCommonSubsequence("abcde","ace")
print(a)
