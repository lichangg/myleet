#!/usr/bin/env python
# -*- coding:utf-8 -*-
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for x in nums:
            heapq.heappush(heap, x)
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap) # [5,6]  从堆中弹出最小的元素


a=Solution().findKthLargest([3,2,1,5,6,4],2)
print(a)