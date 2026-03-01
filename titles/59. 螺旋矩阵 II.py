#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 这题真无聊, 用0,1,2,3  这四个数分别表示右下左上四个方向, 转圈就完事儿了
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dp = [[0] * n for _ in range(n)]
        x, y = 0, 0
        direct = 0
        padding = 0
        for i in range(1, n**2+1):
            dp[x][y] = i
            if direct == 0:
                y+=1
                if y >= n - padding -1:
                    direct = 1

            elif direct == 1:
                x +=1
                if x >= n - padding-1:
                    direct = 2
            elif direct == 2:
                y -= 1
                if y == padding:
                    direct = 3
                    padding +=1
            else:
                x -= 1
                if x == padding:
                    direct = 0
        return dp
a=Solution().generateMatrix(3)
print(a)

