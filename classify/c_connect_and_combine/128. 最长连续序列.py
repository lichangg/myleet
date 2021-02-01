#!/usr/bin/env python
# -*- coding:utf-8 -*-
from collections import Counter
from typing import List

# 完完全全仿照的839题做的,代码几乎一样
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if not n:return 0
        un = UnionFind(n)
        a=set(nums)
        nums = list(a)

        for idx, i in enumerate(nums):
            if i -1 in a:
                un.union(idx, nums.index(i-1))

        # 遍历完数组后合并一下,
        for x in range(n):
            un.find(x)
        a=Counter(un.parent)
        c=a.most_common(1)
        return c[0][1]


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = n

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x,y = self.find(x), self.find(y)
        if x!=y:
            self.count-=1
            self.parent[x] = y
a=Solution().longestConsecutive(nums =[0,0,-1])
print(a)