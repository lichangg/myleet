#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 初始化失败
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dps = [[1 if i == 0 or j ==0 else 0for j in range(n)]for i in range(m)]
        #上面这句和下面有着很大的区别
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 or j==0:
        #             dps[i][j] = 1
        #         else:
        #             dps[i][j] = 0



        for i in range(1,n):
            for j in range(1,m):
                dps[j][i] = dps[j][i-1] + dps[j-1][i]

        return dps[-1][-1]

# 进一步压缩空间 //todo
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

a=Solution().uniquePaths(m = 3, n = 7)
print(a)