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

# 摩尔投票法，时间O（n）空间O（1）
# 由于题目规定了数组中的众数的数量肯定是过半的， 所以本质思想是众数数量和其他所有数的数量互相抵消，最后剩下的就只有众数
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

a = Solution().majorityElement([3,2,3,2,2])
print(a)

