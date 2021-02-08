#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 学到了
# 又是经典动态规划, 初始化第一列和第一行后进行计算
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        # 第一行
        for j in range(1, n2 + 1):
            dp[0][j] = dp[0][j - 1] + 1
        # 第一列
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i - 1][0] + 1
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                # 若该处字符相同,也就是这个字符可以忽略掉,则步骤可回退至i-1,j-1的状态
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # 若该处字符不相同, 首先可以知道的是从[i-1][j]到[i][j]和从[i][j-1]到[i][j]都只需要一步,所以选择[i-1][j]和[i][j-1]中步骤较少也就是数字越小的值+1
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        print(dp)
        return dp[-1][-1]


# 二刷失败, 看题解再写
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = []
        for i in range(len(word1) + 1):
            t = []
            for j in range(len(word2) + 1):
                if j == 0 and i == 0:
                    t.append(0)
                elif j == 0 and i != 0:
                    t.append(i)
                elif i == 0 and j != 0:
                    t.append(j)
                else:
                    t.append(0)
            dp.append(t)
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i][j] - 1)
                else:
                    dp[i + 1][j + 1] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i][j])

        return dp[-1][-1]


# 再刷
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1 = ' ' + word1
        word2 = ' ' + word2
        m = len(word1)
        n = len(word2)
        dp = [[0] * n for _ in range(m)]

        for x in range(m):
            for y in range(n):
                if x == 0:
                    dp[x][y] = y
                elif y == 0:
                    dp[x][y] = x

        i = 1
        while i < m:
            j = 1
            while j < n:
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i-1][j-1])+1
                j += 1
            i += 1
        return dp[-1][-1]

a = Solution().minDistance('horse', 'ros')
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
