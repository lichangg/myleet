#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 大根堆
from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hq = []
        for i in stones:
            heapq.heappush(hq, -i)
        while len(hq) >= 2:
            h1 = heapq.heappop(hq)
            h2 = heapq.heappop(hq)
            if h1-h2 == 0:
                continue
            else:
                heapq.heappush(hq, -abs(h1-h2))

        if not len(hq):
            return 0
        else:
            return -hq[0]


a=Solution().lastStoneWeight([2,3,1])
print(a)