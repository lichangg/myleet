#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 这种动态规划会超时
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = len(s)
        dp = [[0] * l for _ in range(l)]
        for pan in range(l):
            for i in range(l-pan):
                if pan == 0:
                    dp[i][i] = 0
                    continue
                j = i + pan
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i + 1][j]) + 1
        return dp[0][-1]<=1

# 反正只允许删除一个字符, 直接低位对应高位一位一位的验证且允许有一次不对
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = len(s)
        low,high = 0, l-1
        while low<high:
            if s[low] == s[high]:
                low+=1
                high-=1
            else:
                s1 = s[low+1:high+1]
                s2 = s[low:high]
                return s1==s1[::-1] or s2==s2[::-1]
        return True
a=Solution().validPalindrome('abc')
print(a)
