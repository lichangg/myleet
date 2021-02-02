#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        self.has_expirenced = set()

        def dfs(codinate):

            i, j = codinate
            if i < 0 or i >= num_rows or j < 0 or j >= num_cols:
                return
            if grid[i][j] == '1' and (i, j) not in self.has_expirenced:
                self.has_expirenced.add((i, j))
                dfs((i+1, j))
                dfs((i, j+1))
                dfs((i-1, j))
                dfs((i, j-1))
            else:
                return
        count = 0
        i = 0
        while i < num_rows:
            j = 0
            while j < num_cols:
                if grid[i][j] == '1' and (i, j) not in self.has_expirenced:
                    dfs((i, j))
                    count+=1
                j += 1
            i += 1
        return count

#并查集的解法
class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            self.count -= 1

    def getCount(self):
        return self.count

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        uf = UnionFind(grid)
        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                        if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                            uf.union(r * nc + c, x * nc + y)

        return uf.getCount()

a = Solution().numIslands(grid = [["1","1","1"],
                                  ["0","1","0"],
                                  ["1","1","1"]]

)
print(a)
