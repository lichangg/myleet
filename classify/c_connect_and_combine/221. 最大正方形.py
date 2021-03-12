#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 不优雅....好多可以优化的地方
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        self.max_area = 0
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        def dfs(cordinate):
            side = 0
            cur_cordinates = [cordinate]
            while 1:
                tmp = set()
                for _ in range(len(cur_cordinates)):
                    i, j = cur_cordinates.pop()
                    if (0 <= i < num_rows and 0 <= j < num_cols and matrix[i][j] == "1"):
                        will_add = [(i+1, j),(i, j+1),(i+1, j+1)]

                        for point in will_add:
                            if point not in tmp:
                                tmp.add(point)


                    else:
                        self.max_area = max(side * side, self.max_area)
                        return
                else:
                    cur_cordinates = tmp
                    side +=1

        i = 0
        while i < num_rows:
            j = 0
            while j < num_cols:
                if matrix[i][j] == '1':
                    dfs((i, j))
                j+=1
            i+=1
        return self.max_area

# 卧槽,学到了,动态规划
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0

        def exc(l):
            return list(map(int, l))
        # 这行代码是将matrix里面的每个元素都转成int
        dp = list(map(exc, matrix))
        a, b = len(matrix[0]), len(matrix)
        for i in range(1, b):
            for j in range(1, a):
                if dp[i][j] == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
        return max(list(map(max, dp))) ** 2

# 再刷
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        i = 0
        max_side = 0
        while i< m:
            j = 0
            while j<n:
                if i == 0 or j==0:
                    dp[i][j] = 1 if matrix[i][j] == '1' else 0
                    max_side = max(dp[i][j], max_side)
                else:
                    if matrix[i][j] == '1':

                        dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                        max_side = max(dp[i][j], max_side)

                    else:
                        dp[i][j] = 0
                j+=1
            i+=1
        return max_side ** 2
a = Solution().maximalSquare(matrix=[["0","1"],
                                     ["1","0"]])


print(a)
