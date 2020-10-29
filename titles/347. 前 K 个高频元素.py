#!/usr/bin/env python
# -*- coding:utf-8 -*-
import collections
import heapq
from typing import List


# 利用count,实在太慢了
# 执行用时：1992 ms, 在所有 Python3 提交中击败了5.20%的用户
# 内存消耗：16.6 MB, 在所有 Python3 提交中击败了55.34%的用户
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         s_li = set(nums)
#         hasmap = {}
#         for i in s_li:
#             hasmap[i] = nums.count(i)
#         print(hasmap)
#         sort_hasmp = sorted(hasmap, key=lambda x: hasmap[x], reverse=True)
#         res = []
#         print(sort_hasmp)
#         for i in sort_hasmp[:k]:
#             res.append(i)
#         return res

# 自己实现的hashmap保存次数,比count快得多..
# 执行用时：52 ms, 在所有 Python3 提交中击败了68.95%的用户
# 内存消耗：16.4 MB, 在所有 Python3 提交中击败了92.04%的用户
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dit = {}
        for i in nums:  # 使用字典的特性（相同元素后面值的会覆盖前面的值）统计元素的频率，时间复杂度为O(N)
            if i not in dit:  # 如果不存在，则将其存入字典中，此时该值的出现频率为1
                dit[i] = 1
            else:  # 如果已经存在，则其出现频率加1
                dit[i] = dit[i] + 1

        sort_hasmp = sorted(dit, key=lambda x: dit[x], reverse=True)
        res = []
        for i in sort_hasmp[:k]:
            res.append(i)
        return res

# 使用小根堆,python里面的heapq默认是维护最小的在最上面(也就是小根堆),所以频数得取负
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#          #学到了
#         dic = collections.Counter(nums)
#         print(dic)
#         heap, ans = [], []
#         for i in dic:
#             heapq.heappush(heap, (-dic[i], i))
#         for _ in range(k):
#             ans.append(heapq.heappop(heap)[1])
#         return ans
heap = []
for i in [3,1,2,5,8,0,7]:
    heapq.heappush(heap,i)
for i in range(7):
    heapq.heappop(heap)

# b = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]
# a = Solution().topKFrequent(b, 2)
# print(a)
