#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 思路1. 动态规划
# 1. 建立动态规划数组并初始化(数组里面每个元素都是一个容量为2的列表, 其中第一个元素是表示当天不偷能获得的最大值, 第二个元素表示当天偷的话能获得的最大值)
# 2. 构建数组: 当天状态是不偷的话前一天会有偷和不偷两个状态, 当天状态时偷的话前天只能不偷
#
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:return 0
        dp = [[0] * 2 for _ in range(len(nums))]
        dp[0][0], dp[0][1] = 0, nums[0]
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][0] + nums[i]
        return max(dp[-1])

#  思路2.
# 1. 将之前的结果缓存起来
from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache()
        def dp(seq):
            if seq == 0:
                return nums[0]
            elif seq < 0:
                return 0
            elif seq == 1:
                return max(nums[0], nums[1])
            else:
                return max(dp(seq - 2) + nums[seq], dp(seq - 1))

        return dp(len(nums)-1)
a=Solution().rob([2,1,1,2])
print(a)