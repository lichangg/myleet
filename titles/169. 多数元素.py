#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         hashmap = {}
#         for i in nums:
#             hashmap[i] = hashmap.get(i, 0) + 1
#         print(hashmap)
#         a = sorted(hashmap, key=lambda x: hashmap.get(x))
#         return a.pop()

# 别人写的,先排序,然后
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        div, mod = divmod(len(nums), 2)
        if not mod:
            a=div-1
        else:
            a=div
        return nums[a]

a = Solution().majorityElement([3,2,3,2,2])
print(a)

