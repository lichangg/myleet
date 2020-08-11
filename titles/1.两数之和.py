#!/usr/bin/env python
# -*- coding:utf-8 -*-
# class Solution:
#     def twoSum(self, nums: list, target: int):
#
#         for index, i in enumerate(nums):
#             if target - i in nums and index != nums.index(target - i):
#                 return [index, nums.index(target - i)]

# class Solution:
#     def twoSum(self, nums, target):
#         hashmap = {}
#         for i, num in enumerate(nums):
#             if hashmap.get(target - num) is not None:
#                 return [i, hashmap.get(target - num)]
#             hashmap[num] = i

class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for index, num in enumerate(nums):
            hashmap[num] = index
        print(hashmap)
        for index, num in enumerate(nums):
            aim = target - num
            if hashmap.get(aim, index) != index:
                return [index, hashmap.get(aim)]


a=Solution().twoSum([3,2,4], 6)
print(a)