#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 思路1 滑动窗口
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        window_start = 0
        window_end = 0
        while window_end <= len(nums)-1:
            cur_sum = sum(nums[window_start:window_end+1])
            max_sum = max(max_sum,cur_sum)
            window_end+=1
            if cur_sum<=0:
                window_start =window_end
        return max_sum

# 用一个pre优化一下
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        window_end = 0
        pre = 0
        while window_end <= len(nums)-1:

            cur_sum = pre + nums[window_end]
            pre = cur_sum
            max_sum = max(max_sum,cur_sum)
            window_end+=1
            if cur_sum<=0:
                pre = 0
        return max_sum










a=Solution().maxSubArray([-2])
print(a)