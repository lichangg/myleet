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






a=Solution().lengthOfLIS([10,9,2,5,3,7,101,18])
print(a)