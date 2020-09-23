#!/usr/bin/env python
# -*- coding:utf-8 -*-
import heapq
from typing import List
# 堆是一种完全二叉树
# 构建一个小根堆，该数据结构的特点是始终将最小的放在第0个元素上，之后的元素并不保证
# 用小根堆找第K大的元素,666
# 思路就是堆的容量只装k个元素, 再想往里面添加就得弹出最小的
# 把列表中所有元素都处理后, 再弹一个堆元素,该元素就是第K大的元素
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for x in nums:
            heapq.heappush(heap, x)
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap) # [5,6]  从堆中弹出最小的元素

# # 二刷, 不过这样意义不大
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         nums.sort(reverse=True)
#         return nums[k-1]
# # 二刷,小根堆, 因为heapq只能构建小根堆, 所以把所有元素取负就能够构建大根堆,妙啊
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         import heapq
#         stack = []
#         for i in nums:
#             heapq.heappush(stack, -i)
#         for i in range(k-1):
#             heapq.heappop(stack)
#         return -heapq.heappop(stack)
a=Solution().findKthLargest([3,2,1,5,6,4],2)
print(a)