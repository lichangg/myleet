#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 用动态规划遇到[25000,24999,24998,...,3,2,1]这种会超时
class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [(0, False)] * l
        dp[0] = (0, True)
        i = 0
        while i<l:
            for j in range(1, nums[i]+1):
                if i+j>=l:
                    break

                if dp[i+j][1] == False:
                    dp[i+j] = (dp[i][0]+1, True)
                else:
                    dp[i+j] = (min(dp[i+j][0], dp[i+j][0]+1), True)

            i+=1
        return dp[-1][0]

# 贪心, 不断的更新能达到的最大位置
class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        cur, max_pos, step = 0,0,0
        for idx, n in enumerate(nums):
            if idx > cur:
                step+=1
                cur = max_pos
            max_pos = max(max_pos, idx+n)
            if max_pos>=l-1:
                return step+1

a=Solution().jump([2,3,1,1,4])
print(a)

