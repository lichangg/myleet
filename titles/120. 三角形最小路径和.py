#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 思路: 动态规划+递归
# 1. 设置recur(idx, raw_idx)表示第raw_idx行的第idx个节点能够返回的最小的值
# 2. 该最小值往下可以有两个来源:
#   - 一个是recur(idx, raw_idx + 1)
#   - 另一个是recur(idx+1, raw_idx + 1)
# 3. 取这两个来源的更小值, 加上本节点数值就是本节点能返回的最小值
# 4. 另外还需要用缓存存储已经计算过的节点最小值数据, 不然会超时(动态规划)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.cache = {}
        if not triangle:return 0
        def recur(idx, raw_idx):
            if (idx, raw_idx) in self.cache: return self.cache[idx, raw_idx]
            if raw_idx>len(triangle)-1 or idx >= len(triangle[raw_idx]):
                return 0
            s1 = recur(idx, raw_idx + 1)
            s2 = recur(idx + 1, raw_idx + 1)
            cur_min = min(s1, s2) + triangle[raw_idx][idx]
            self.cache[(idx, raw_idx)] = cur_min
            return cur_min
        return recur(0,0)

a=Solution().minimumTotal(
[[-1],[-2,-3]])
print(a)