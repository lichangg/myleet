#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 自己写的完全递归，意思就是
# (m,n)=(m,n-1)+(m-1,n)
# (m,n-1)=(m-1,n-1)+(m,n-2)
# (m-1,n)=(m-1,n-1)+(m-2,n)
# 看到没，(m-1,n-1)算了两次，和青蛙跳台阶一样，其实可以保存这个算了两次的量
# 没有利用动态规划，直接超时
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         def wrap(m, n):
#
#             if m == 1 and n == 1:
#                 return 0
#             if m == 1 or n == 1:
#                 return 1
#             return wrap(m - 1, n) + wrap(m, n - 1)
#
#         if m == 1 and n == 1:
#             return 1
#         else:
#             return wrap(m,n)

# 结合一下矩阵的思路从矩阵的[0,1]和[1,0]坐标开始填到达该位置的方法数，直到填满整个矩阵，最后直接拿[m-1,n-1]坐标的值就行了
# 这样就是保存所有点的方法数，其实没必要，而且我还填失败了，好难想
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         if m == 1 and n == 1:
#             return 1
#         matrix = [[None for _ in range(m)] for __ in range(n)]
#         matrix[0][1],matrix[1][0] = 1,1
#         def dg(a,b):
#             if a ==m+1 or b==n+1:
#                 return
#             matrix[a][b] = matrix[a-1][b] + matrix[a][b-1]
#             dg(a,b+1)
#             dg(a+1,b)
#         dg(1,1)
#
#         return matrix[m-1][n-1]

# 这个也太难想了，空间压缩到了一维的
# 原理是当处在当前坐标时，自己的上一个已经改掉了，【之前】的当前位置加上上一个位置的值就可以赋值给【目前】的当前位置
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [1 for i in range(n)]
        for k in range(1, m):
            for j in range(1, n):
                matrix[j] += matrix[j - 1]

        return matrix[-1]


# 学到了
# 我真傻啊，之前还想着递归去填每个位置的方法数，直接for循环填不香么，这种方式是竖着填下来的
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         matrix = [[0 for i in range(n)] for j in range(m)]
#         for k in range(m):
#             for j in range(n):
#                 if k-1 < 0:
#                     matrix[k][j] = 1
#                 elif j-1 < 0:
#                     matrix[k][j] = 1
#                 else:
#                     matrix[k][j] = matrix[k-1][j] + matrix[k][j-1]
#         return matrix[m-1][n-1]

# 二刷,横着填dp数组,不过没进行空间压缩
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 if i == 0 or j == 0 else 0 for j in range(m)] for i in range(n)]
        i=1
        j=1
        while i < n:
            while j < m:
                dp[i][j] = dp[i][j - 1] + dp[i-1][j]
                j+=1
            j=1
            i+=1
        return dp[-1][-1]

a = Solution().uniquePaths(3, 2)
print(a)
