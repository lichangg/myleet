#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

# 暴力法加动态规划
# 1. 状态定义: dp[i]是前i个子序列的最长子序列长度
# 2. 状态转移: dp[i] = max(dp[i], dp[j] + 1) for j in [0, i)
# 3. 初始都为1
# Dynamic programming.
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                # 内循环是j递增后恒定和i比较, 因为每次都取了max,所以处在任一一个j的位置,它都得
                # 战胜之前最大的dp[i]才能+1
                if nums[j] < nums[i]: # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

# 企图用动态规划+单调栈失败
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         if not nums: return 0
#         dp = [1] * len(nums)
#         stack = []
#         for i in range(len(nums)):
#             if nums[i] > nums[i-1]:
#                 dp[i] = dp[i-1] + 1
#                 stack.append(i)
#             else:
#                 tmp_stack = []
#                 while stack and nums[stack[-1]] < nums[i]:
#                     idx = stack.pop()
#                     tmp_stack.append(dp[idx])
#                 dp[i] = max(tmp_stack) + 1 if tmp_stack else 1
#                 stack.append(i)
#         return dp[-1]


# a=Solution().lengthOfLIS([10,9,2,5,3,7,101,18])
a=Solution().lengthOfLIS([0,1,0,3,2,3])
print(a)