#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 终极土办法
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        n = 0
        while i < len(nums):
            if nums[i] < 1:
                i += 1
                continue
            if i != 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            if n + 1 != nums[i]:
                return n + 1

            n += 1
            i += 1
        else:
            return n + 1

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1

        nums = set(nums)
        set_nums = set(nums)
        if len(set_nums)== 1 and set_nums.pop() == 1:
            return 2
        i = 0

        while i < len(nums):
            if i+1 not in set_nums:
                return i+1
            else:
                i+=1
        else:
            return i+1

a = Solution().firstMissingPositive([1,2,3])
print(a)
