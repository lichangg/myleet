#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 这种解法会超时,复杂度位O(2**N)
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.S =S
        self.count = 0
        def dfs(nums, s):
            if not nums:
                if s == self.S:
                    self.count+=1
                    return
                else:
                    return
            cur = nums.pop()

            dfs(nums[:], s+cur)
            dfs(nums[:], s-cur)
        dfs(nums,0)
        return self.count

# 转换成0-1背包问题,和416题一样的思路,只不过416题的target是0, 这个题的target是给定的S,学到了
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if sum(nums) < S or (sum(nums) + S) % 2 == 1: return 0
        P = (sum(nums) + S) // 2
        dp = [1] + [0 for _ in range(P)]
        for num in nums:
            for j in range(P,num-1,-1):dp[j] += dp[j - num]
        return dp[P]

a=Solution().findTargetSumWays([16,40,9,17,49,32,30,10,38,36,31,22,3,36,32,2,26,17,30,47],49)
print(a)