#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        nums.sort()
        i = 0
        max_dis = float('-inf')
        while i<=len(nums)-2:
            max_dis = max(nums[i+1] -nums[i] , max_dis)
            i+=1
        return max_dis

a=Solution().maximumGap([3,4,6,1])
print(a)