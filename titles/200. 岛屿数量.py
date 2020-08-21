#!/usr/bin/env python
# -*- coding:utf-8 -*-
import collections
from typing import List
# 连通型问题都可以用DFS或BFS扩张来解决

# DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        x = len(grid) - 1
        y = len(grid[0]) - 1
        if x == 0 and y == 0:
            return 1 if grid[0][0] == '1' else 0
        def dps(m, n):
            # 直接判断边界外的还有0的情况返回
            if m == -1 or n == -1 or m>x or n >y or grid[m][n] =='0':return
            grid[m][n] = '0'
            prob_coordinate = [(m + 1, n), (m - 1, n), (m, n + 1), (m, n - 1)]
            for co in prob_coordinate:
                dps(co[0], co[1])

        count = 0
        for i in range(x + 1):
            for j in range(y + 1):
                if grid[i][j] == '1':
                    dps(i, j)
                    count+=1
        return count
# BFS(这是BFS么?有点怀疑)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':  # 发现陆地
                    count += 1  # 结果加1
                    grid[row][col] = '0'  # 将其转为 ‘0’ 代表已经访问过
                    # 对发现的陆地进行扩张即执行 BFS，将与其相邻的陆地都标记为已访问
                    # 下面还是经典的 BFS 模板
                    land_positions = collections.deque()
                    land_positions.append([row, col])
                    while len(land_positions) > 0:
                        x, y = land_positions.popleft()
                        for new_x, new_y in [[x, y + 1], [x, y - 1], [x + 1, y], [x - 1, y]]:  # 进行四个方向的扩张
                            # 判断有效性
                            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == '1':
                                grid[new_x][new_y] = '0'  # 因为可由 BFS 访问到，代表同属一块岛，将其置 ‘0’ 代表已访问过
                                land_positions.append([new_x, new_y])
        return count


b = [["1","1","0","0","0"]
    ,["1","1","0","0","0"]
    ,["0","0","1","0","0"]
    ,["0","0","0","1","1"]
     ]

a = Solution().numIslands(b)
print(a)
