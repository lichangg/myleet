#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# BFS失败
# class Solution:
#     def swimInWater(self, grid: List[List[int]]) -> int:
#         i = 0
#         # while i<len(grid):
#         #     j = 0
#         #     while j< len(grid[0]):
#         #         if i==0 and j==0:
#         #             pass
#         #         elif i == 0:
#         #             dp[0][j] = max(dp[0][j],dp[0][j-1])
#         #         elif j == 0:
#         #             dp[i][0] = max(dp[i][0],dp[i-1][0])
#         #         else:
#         #             dp[i][j]= min(max(dp[i][j], dp[i-1][j]),max(dp[i][j],dp[i][j-1]))
#         #         j+=1
#         #     i+=1
#         self.ma_list = []
#         self.got = set()
#
#         def dfs(path, cordinate, pre_co):
#             i, j = cordinate
#             if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1:
#                 return
#             newpath = path[:]
#             newpath.append(grid[i][j])
#             if j == len(grid[0]) - 1 and i == len(grid) - 1:
#                 self.ma_list.append(max(newpath))
#             for co in [(i + 1, j), (i, j + 1), (i, j - 1), (i-1, j)]:
#
#                 if co != pre_co:
#                     if grid[co[0]][co[1]]<=max(newpath):
#                         dfs(newpath, co, cordinate)
#
#
#         dfs([], (0, 0), None)
#         return min(self.ma_list)
# 重点！！！
# 这题我学到了，此题的核心思路在于寻找到在所有从左上到右下的路线中，经历过的最大的数字最小的路线
# 首先可以维护一个小根堆，小根堆里面存的是（当前数字，当前坐标）
# 初始小根堆里面放的是左上角的点
# 然后开始pop，pop出来的点接下来有上下左右四个方向可以走，把它们全部push进堆中，
# 继续pop，这样可以保证总是先弹出更小的点，若由该点生产的坐标出了几个大数，那么再弹出来的就是之前推进去的小一些的数
# （含义为若当前数之后要走的的数过大，就得返回去从另外一个小的数走）
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        hq = [(grid[0][0],(0,0))]
        visited = set()
        visited.add((0,0))
        max_ = 0
        while hq:
            cur_num, cur_cordinate = heapq.heappop(hq)
            max_ = max(cur_num,max_)
            x, y = cur_cordinate
            if x == len(grid)-1 and y == len((grid[0]))-1:
                return max_
            for co in [(x + 1, y), (x, y + 1), (x, y - 1), (x-1, y)]:
                if co not in visited:
                    i,j=co
                    if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1:
                        continue
                    else:
                        visited.add(co)
                        heapq.heappush(hq, (grid[i][j], co))



a = Solution().swimInWater(
    [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
    )
print(a)
