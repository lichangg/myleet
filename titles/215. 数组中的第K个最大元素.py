#!/usr/bin/env python
# -*- coding:utf-8 -*-
import heapq
from typing import List
# 堆是一种完全二叉树
# 构建一个小根堆，该数据结构的特点是始终将最小的放在第0个元素上，之后的元素并不保证
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