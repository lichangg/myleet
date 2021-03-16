#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:

        self.all_count = 0
        self.in_count = 0
        self.direct = [(2.)]
        self.step = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        def dfs(n, k, r, c, step):
            r += step[0]
            c += step[0]
            if k <= 0:
                return
            if r < 0 or c < 0 or r > n - 1 or c > n - 1:
                return
            else:
                self.in_count += 1
                for step in self.step:
                    dfs(n, k - 1, r, c, step)

        for step in self.step:
            self.all_count += 8
            dfs(N, K - 1, r, c, step)
        return self.in_count / self.all_count
a=Solution().knightProbability(1,0,0,0)
print(a)