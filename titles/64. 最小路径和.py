#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 理解了62题的思想这题就很简单了，以后试试看能不能降到1维
class Solution:
    def minPathSum(self, grid) -> int:
        n = len(grid)
        m = len(grid[0])
        matrix = [[None for j in range(m)] for i in range(n)]
        matrix[0][0] = grid[0][0]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    matrix[0][j] = matrix[0][j - 1] + grid[0][j]
                elif j == 0:
                    matrix[i][0] = matrix[i - 1][0] + grid[i][0]
                else:
                    cur_min = min(matrix[i][j - 1], matrix[i - 1][j])
                    matrix[i][j] = cur_min + grid[i][j]

        return matrix[n - 1][m - 1]


# 二刷成功将空间降到1维
class Solution:
    def minPathSum(self, grid) -> int:
        if not grid or not grid[0]:
            return 0
        dp = []
        for index, n in enumerate(grid[0]):
            if index == 0:
                dp.append(n)
            else:
                dp.append(dp[index-1] + n)
        i = 1
        while i < len(grid):
            j = 0
            while j < len(grid[0]):
                if j == 0:
                    dp[j] = dp[j] + grid[i][0]
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
                j += 1
            i += 1
            print(dp)
        return dp[-1]

# 再刷, 直接路径压缩一步到位
class Solution:
    def minPathSum(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        if not n:
            return 0
        i= 1
        initial = 0
        res = []
        for x in grid[0]:
            initial+=x
            res.append(initial)
        while i<m:
            j = 0
            while j<n:
                if j == 0:
                    res[0] = grid[i][0] + res[0]
                    j+=1
                    continue

                res[j] = min(res[j], res[j-1]) + grid[i][j]

                j+=1
            i+=1
        return res[-1]
a = Solution().minPathSum([[]])
print(a)
