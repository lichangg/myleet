#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 思路1. 动态规划,仍然败在了初始化上
class Solution:
    def minPathSum(self, grid) -> int:
        if not grid or not grid[0]:
            return 0

        rows, columns = len(grid), len(grid[0])
        dps = [[0] * columns for _ in range(rows)]
        dps[0][0] = grid[0][0]
        for i in range(1, rows):
            dps[i][0] = dps[i - 1][0] + grid[i][0]
        for j in range(1, columns):
            dps[0][j] = dps[0][j - 1] + grid[0][j]


        i=1
        while i<len(grid):
            j=1
            while j<len(grid[i]):
                dps[i][j] = min(dps[i-1][j], dps[i][j-1]) + grid[i][j]
                j+=1
            i+=1
        return dps[-1][-1]


a=Solution().minPathSum(grid =  [[1,3,1],[1,5,1],[4,2,1]])
print(a)
