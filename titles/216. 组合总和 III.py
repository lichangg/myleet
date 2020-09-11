#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 每日一题, 过是能过,1660ms,可优化的地方比较多
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        self.l = [1,2,3,4,5,6,7,8,9]
        # 加了缓存竟然更慢了,不太理解
        self.mem = {}
        def dfs(n, use_num, k, path):
            path.append(use_num)
            if k<0 or n<0:
                return

            if k == 0 and n == 0:
                path.sort()
                if str(path) not in self.mem:
                    self.mem[str(path)] = 1
                    self.res.append(path)
            for i in self.l:
                if i not in path:
                    dfs(n-i, i, k-1, path[:])
        for i in self.l:
            dfs(n-i, i, k-1,[])
        return self.res

# 放弃动态规划
# class Solution:
#     def combinationSum3(self, k: int, n: int) -> List[List[int]]:
#         self.l = [1,2,3,4,5,6,7,8,9]
#         dp = [[[]for _ in range(n+1)] for _ in range(k)]
#         dp[]


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        self.l = [1,2,3,4,5,6,7,8,9]
        # 加了缓存竟然更慢了,不太理解
        self.mem = {}
        def dfs(n, use_num, k, path,begin_index):
            path.append(use_num)
            if k<0 or n<0:
                return

            if k == 0 and n == 0:
                self.res.append(path)


                # 就这一步的优化和添加begin_index就优化到位了
                return

            for index, i in enumerate(self.l):
                if index> begin_index:
                    dfs(n-i, i, k-1, path[:], index)
        for index, i in enumerate(self.l):
            dfs(n-i, i, k-1,[], index)
        return self.res
a=Solution().combinationSum3(3,7)
print(a)
