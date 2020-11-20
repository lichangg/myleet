#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 该题有个推论:
# 总加油量>=总耗油量一定有解,反之一定无解
from typing import List

# 一刷, 暴力法
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        def func(n):
            remain = 0
            j = n
            while j < len(gas):
                remain += gas[j]
                if remain >= cost[j]:
                    remain -= cost[j]
                    j+=1
                else:
                    return
            i = 0
            while i<n:
                remain += gas[i]
                if remain >= cost[i]:
                    remain -= cost[i]
                    i+=1
                else:
                    return
            return n
        for idx in range(len(gas)):
            if func(idx) != None:
                return idx
        else:
            return -1
a=Solution().canCompleteCircuit([3,1,1],[1,2,2])
print(a)
