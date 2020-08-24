#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 列表有个非常好用的函数:count
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return list({x for x in set(nums) if nums.count(x) > len(nums)/3})

a=Solution().majorityElement([1,1,1,3,3,2,2,2])
print(a)