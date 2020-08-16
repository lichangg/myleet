#!/usr/bin/env python
# -*- coding:utf-8 -*-
#理解了62题的思想这题就很简单了，以后试试看能不能降到1维
class Solution:
    def minPathSum(self, grid) -> int:
        n = len(grid)
        m = len(grid[0])
        matrix = [[None for j in range(m)] for i in range(n)]
        matrix[0][0] = grid[0][0]
        for i in range(n):
            for j in range(m):
                if i == 0 and j==0:
                    continue
                if i == 0:
                    matrix[0][j] = matrix[0][j-1] + grid[0][j]
                elif j==0:
                    matrix[i][0] = matrix[i-1][0] + grid[i][0]
                else:
                    cur_min = min(matrix[i][j-1], matrix[i-1][j])
                    matrix[i][j] = cur_min + grid[i][j]

        return matrix[n-1][m-1]
a=Solution().minPathSum([
  [1,2,5],
  [3,2,1],
])
print(a)
