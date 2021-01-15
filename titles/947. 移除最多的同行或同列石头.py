#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List
from functools import lru_cache
# 思路1. 找到孤立的块(是点也行), 也就是它不能被任何一个点或块连起来,孤立块的数量也就是必须得留下来的数量, 而用总数减这些块的数量就是可以移动的最大的数量
# 1. 难点在于联通, 此处实现的联通复杂度太高了
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # l = len(stones)
        # @lru_cache(l)
        self.cache = {}
        def relate(idx):
            tmp = set()
            def expand(idx):
                for new_idx, i in enumerate(stones):
                    if new_idx not in tmp:
                        if i[0] == stones[idx][0] or i[1] == stones[idx][1]:
                            tmp.add(idx)
                            expand(new_idx)
            expand(idx)
            return tmp

        relative = []
        for idx, i in enumerate(stones):
            for rela in relative:
                if idx in rela:
                    break
            else:
                relate_idx = relate(idx)
                relative.append(relate_idx)


        return len(stones) - len(relative)

# 思路2. 优化一下联通的算法
a=Solution().removeStones(
[[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]])
print(a)

if __name__ == "__main__":
    stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2],[3,3]]
    def relate(idx):
        cache = {}
        for idx, i in enumerate(stones):
            for idx_j, j in enumerate(stones):
                if i[0] == j[0] or i[1] == j[1]:
                    if idx in cache:
                        cache[idx].append(idx_j)
                    else:
                        cache[idx_j] = [idx_j]
        print(cache)
    print(relate(0))