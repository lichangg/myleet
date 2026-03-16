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







"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组是数组中的一个连续部分。

 

示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：

输入：nums = [1]
输出：1
示例 3：

输入：nums = [5,4,-1,7,8]
输出：23

"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        dp = [0] * len(nums)
        dp[0] = nums[0]
        i = 1
        while i < len(nums):
            if dp[i-1] >= 0:
                dp[i] = nums[i] + dp[i-1]
            else:
                dp[i] = nums[i]
            i+=1
        return max(dp)

a=Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(a)