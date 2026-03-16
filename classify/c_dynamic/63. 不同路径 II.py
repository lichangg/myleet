#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if n == 0:return 0
        dp = [[1] * n for _ in range(m)]
        i = 0
        while i< m:
            j = 0
            while j<n:
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 and j == 0:
                    dp[0][0] = 1
                elif i == 0:
                    dp[0][j] = dp[0][j-1]
                elif j == 0:
                    dp[i][0] = dp[i-1][0]
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
                j+=1
            i+=1
        return dp[-1][-1]
"""
给定一个 m x n 的整数数组 grid。一个机器人初始位于 左上角（即 grid[0][0]）。机器人尝试移动到 右下角（即 grid[m - 1][n - 1]）。机器人每次只能向下或者向右移动一步。

网格中的障碍物和空位置分别用 1 和 0 来表示。机器人的移动路径中不能包含 任何 有障碍物的方格。

返回机器人能够到达右下角的不同路径数量。
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:


a=Solution().uniquePathsWithObstacles([[]])
print(a)