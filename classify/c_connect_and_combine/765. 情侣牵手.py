#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

from collections import Counter

#自己写的并查集,本地很快,线上老是超时
# class Solution:
#     def minSwapsCouples(self, row: List[int]) -> int:
#         i = 0
#         n = len(row)
#         un = Union(n)
#
#         while i < n - 1:
#             # if row[i] % 2 == 0:
#             #     j = row[i] + 1
#             # else:
#             #     j = row[i] - 1
#             j = row[i] ^ 1
#             if row[i + 1] == j:
#                 un.union(i, i + 1)
#                 continue
#
#             j_idx = row.index(j)
#             un.union(i, j_idx)
#             un.union(i, i + 1)
#             j2 = row[i+1] ^ 1
#             j2_idx = row.index(j2)
#             un.union(i, j2_idx)
#
#             i += 2
#         for x in range(n):
#             un.find(x)
#
#         colony = Counter(un.parent)
#         count = 0
#         for k, v in colony.items():
#             count += v // 2 - 1
#         return count
#
#
# class Union:
#     def __init__(self, n):
#         self.parent = list(range(n))
#
#     def find(self, x):
#         if self.parent[x] == x:
#             return x
#         self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]
#
#     def union(self, x, y):
#         x, y = self.find(x), self.find(y)
#         if x != y:
#             self.parent[x] = y

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        # 贪心算法
        n, res = len(row), 0
        for i in range(0, n, 2):  # 遍历所有座位对的第一个人
            # 这个找另一半的方法确实骚
            mate = row[i] ^ 1  # 它的另一半为当前值异或1即将最后一位取反
            if row[i+1] != mate:  # 如果此时坐的不是它的另一半
                j = i+2+row[i+2:].index(mate)  # 找到它的另一半，直接从i+2找起节省时间
                row[i+1], row[j], res = row[j], row[i+1], res+1  # 交换
        return res


a = Solution().minSwapsCouples(
[1,4,0,5,8,7,6,3,2,9])
print(a)
