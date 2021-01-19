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

a = Solution().numIslands(grid = [["1","1","1"],
                                  ["0","1","0"],
                                  ["1","1","1"]]

)
print(a)
