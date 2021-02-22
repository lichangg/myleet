#!/usr/bin/env python
# -*- coding:utf-8 -*-
#再刷
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:return 0
        l1=len(text1)
        l2=len(text2)
        dp = [[0]*l2 for _ in range(l1)]
        i = 0
        while i<l1:
            j=0
            while j<l2:
                if i == 0 and j == 0:
                    dp[0][0] = 1 if text1[0] == text2[0] else 0
                elif i == 0:
                    dp[0][j] = 1 if text1[0] == text2[j] else dp[i][j-1]
                elif j == 0:
                    dp[i][0] = 1 if text1[i] == text2[j] else dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-1]+1 if text1[i] == text2[j] else max(dp[i][j-1], dp[i-1][j])

                j+=1
            i+=1
        return dp[-1][-1]

a=Solution().longestCommonSubsequence(text1 = "", text2 = "def" )
print(a)