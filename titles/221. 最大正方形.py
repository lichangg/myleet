#!/usr/bin/env python
# -*- coding:utf-8 -*-
import itertools
from typing import List


# 和85，84题一脉相承，就是速度好像太慢了
# 执行用时：400 ms, 在所有 Python3 提交中击败了5.05%的用户
# 内存消耗：14.3 MB, 在所有 Python3 提交中击败了74.00%的用户
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        temp = [[0 for x in range(n)] for y in range(m)]
        for i in range(m):

            for j in range(n):
                if matrix[i][j] != '0':
                    temp[i][j] = temp[i - 1][j] + 1 if i > 0 else 1
                else:
                    temp[i][j] = 0
        max_area = 0
        print(temp)
        for l in temp:
            area = self.findmax(l)
            max_area = max(max_area, area)
        return max_area

    def findmax(self, heights):
        res = 0
        n = len(heights)
        for i in range(n):
            left_i = i
            right_i = i

            while left_i >= 0 and heights[left_i] >= heights[i]:
                left_i -= 1
            while right_i < n and heights[right_i] >= heights[i]:
                right_i += 1
            d = right_i - left_i - 1
            b = min(d, heights[i])
            res = max(res, b * b)
        return res

    # 求连续相同的方法是不行的，因为[3,2]就不连续，3可以参与2的面积
    # def findmax(self, heights):
    #     a=[(k,len(list(v))) for k, v in itertools.groupby(heights)]
    #     res = 0
    #     for i in a:
    #         res = max(res, min(i) * min(i))
    #     return res


# 暴力法是最简单直观的做法，具体做法如下：
# 1. 遍历矩阵中的每个元素，每次遇到 1，则将该元素作为正方形的左上角；
# 2. 确定正方形的左上角后，根据左上角所在的行和列计算可能的最大正方形的边长（正方形的范围不能超出矩阵的行数和列数），在该边长范围内寻找只包含 11 的最大正方形；
# 3. 每次在下方新增一行以及在右方新增一列，判断新增的行和列是否满足所有元素都是 11。

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    # 遇到一个 1 作为正方形的左上角
                    maxSide = max(maxSide, 1)
                    # 计算可能的最大正方形边长
                    currentMaxSide = min(rows - i, columns - j)
                    for k in range(1, currentMaxSide):
                        # 判断新增的一行一列是否均为 1
                        flag = True
                        if matrix[i + k][j + k] == '0':
                            break
                        for m in range(k):
                            if matrix[i + k][j + m] == '0' or matrix[i + m][j + k] == '0':
                                flag = False
                                break
                        if flag:
                            maxSide = max(maxSide, k + 1)
                        else:
                            break

        maxSquare = maxSide * maxSide
        return maxSquare


# 动态规划，遍历每一个位置，如果为1，得到它的最大边长，最大边长就是最大正方形
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    # 这个是在初始化
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        # 这个逻辑很精髓啊, 每一个最右下角的点的dp值(也就是正方形的边长)都由和它关联的 上\下\左上 这三个点当中的最小值+1组成
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])

        maxSquare = maxSide * maxSide
        return maxSquare

# 二刷, 思路没问题, 联通问题可以通过更改其原本的值来防止重复走, 但是需要注意,如果单纯把符合要求的1改成不合要求的0会有问题
# 例如[["0","0","0","1"],
    # ["1","1","0","1"],
    # ["1","1","1","1"],
    # ["0","1","1","1"],
    # ["0","1","1","1"]]
    #在执行matrix[1][0] 的时候会把[2][1]改为0, 会导致在执行到matrix[2][1]的时候,它不合要求了, 所以下面的算法实际上改成了2(其实也没必要改了, 已修改,和重复走是一样的复杂度了)
# 执行用时：600 ms, 在所有 Python3 提交中击败了5.05%的用户
# 内存消耗：14.3 MB, 在所有 Python3 提交中击败了6.35%的用户
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        n = len(matrix)#4
        m = len(matrix[0])#4
        self.max_area = 0

        def valid(y, x):
            return matrix[y][x] == '1'

        def dfs(side, need_valid, imax, jmax):

            self.max_area = max(self.max_area, side ** 2)
            if imax >= n or jmax >= m:
                return
            if all([valid(*i) for i in need_valid]):
                next_valid = []
                for cor in need_valid:
                    if cor[0] == imax and cor[1] == jmax:
                        next_valid.append((imax + 1, jmax + 1))
                        next_valid.append((imax, jmax + 1))
                        next_valid.append((imax + 1, jmax))
                        continue
                    if cor[0] == imax:
                        next_valid.append((cor[0] + 1, cor[1]))
                        continue
                    if cor[1] == jmax:
                        next_valid.append((cor[0], cor[1] + 1))
                        continue
                dfs(side + 1, next_valid, imax + 1, jmax + 1)
            else:
                return

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    need_valid = [(i + 1, j), (i, j + 1), (i + 1, j + 1)]
                    dfs(1, need_valid, i + 1, j + 1)

        return self.max_area
a = Solution().maximalSquare(
    [["1", "1", "1", "0", "0"],
     ["1", "1", "1", "0", "0"],
     ["1", "1", "1", "1", "1"],
     ["0", "1", "1", "1", "1"],
     ["0", "1", "1", "1", "1"],
     ["0", "1", "1", "1", "1"]
     ]
)
print(a)
