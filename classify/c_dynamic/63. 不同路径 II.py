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

a=Solution().uniquePathsWithObstacles([[]])
print(a)