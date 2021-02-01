#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 失败
# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         m = len(board)
#         n = len(board[0])
#         def dfs(coordinate, path, board):
#             i, j = coordinate
#             if i<0 or i>=m or j<0 or j>=n:
#                 return
#
#             if board[i][j] == 'O' and coordinate not in path:
#                 if i == 0 or i == m or j==0 or j==n:
#                     return path
#                 else:
#                     board[i][j] = 'X'
#                     path.add(coordinate)
#
#                 for co in [(i+1, j),(i-1,j),(i,j+1),(i,j-1)]:
#                     dfs(co, path, board)
#
#
#         for i in range(m):
#             for j in range(n):
#                 if board[i][j] == 'O':
#                     path = set()
#                     dfs((i, j), path, board)


# 没那么复杂,从边界出发简单得多
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        n, m = len(board), len(board[0])

        def dfs(x, y):
            if not 0 <= x < n or not 0 <= y < m or board[x][y] != 'O':
                return

            board[x][y] = "A"
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)

        for i in range(m - 1):
            dfs(0, i)
            dfs(n - 1, i)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"


