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

"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

 

示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[0] * 2 for _ in range(len(nums))]
        dp[0][0], dp[0][1] = 0, nums[0]
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][0] + nums[i]

        return max(dp[-1])
a=Solution().rob([2,1,1,2])
print(a)