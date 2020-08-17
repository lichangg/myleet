#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 又是经典动态规划, 初始化第一列和第一行后进行计算
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
                # 若该处字符相同,也就是这个字符可以忽略掉,则步骤可回退至i-1,j-1的状态
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                # 若该处字符不相同, 首先可以知道的是从[i-1][j]到[i][j]和从[i][j-1]到[i][j]都只需要一步,所以选择[i-1][j]和[i][j-1]中步骤较少也就是数字越小的值+1
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1] ) + 1
        print(dp)
        return dp[-1][-1]

a=Solution().minDistance('horse','ros')
print(a)

'''
   '' r  o  s
'' 0, 1, 2, 3
h  1, 1, 2, 3
o  2, 2, 1, 2
r  3, 2, 2, 2
s  4, 3, 3, 2
e  5, 4, 4, 3
'''