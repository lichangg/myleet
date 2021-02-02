#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        self.expireced = set()
        self.max_area = 0
        def dfs(coordinate, path, area):
            i, j = coordinate
            if i < 0 or i > m-1 or j < 0 or j > n-1 or grid[i][j] == 0:
                return

            self.expireced.add(coordinate)
            area+=1
            self.max_area = max(area, self.max_area)
            path.append(coordinate)
            for co in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if co not in self.expireced:
                    dfs(co,  path, area)

        i = 0
        while i < m:
            j = 0
            while j < n:
                if grid[i][j] == 1 and (i, j) not in self.expireced:
                    p = []
                    dfs((i, j), p, 0)
                    self.max_area = max(len(p), self.max_area)
                j+=1
            i += 1
        return self.max_area

# 别人写的dfs,很简洁
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(gird, i, j):
            if 0<=i<m and  0<=j<n and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(grid, i+1,j) + dfs(grid, i-1, j) + dfs(grid, i, j+1) + dfs(grid, i, j-1)
            return 0
        result = 0
        for x in range(m):
            for y in range(n):
                result = max(result, dfs(grid, x, y))
        return result

a=Solution().maxAreaOfIsland(
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    )

print(a)