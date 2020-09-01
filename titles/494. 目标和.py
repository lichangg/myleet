#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


# 这种解法会超时,复杂度位O(2**N)
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.S = S
        self.count = 0

        def dfs(nums, s):
            if not nums:
                if s == self.S:
                    self.count += 1
                    return
                else:
                    return
            cur = nums.pop()

            dfs(nums[:], s + cur)
            dfs(nums[:], s - cur)

        dfs(nums, 0)
        return self.count


# 我们假设P是正子集，N是负子集。让我们看看如何将其转换为子集求和问题：
#                   sum(P) - sum(N) = target
#                   （两边同时加上sum(P)+sum(N)）
# sum(P) + sum(N) + sum(P) - sum(N) = target + sum(P) + sum(N)
#             (因为 sum(P) + sum(N) = sum(nums))
#                        2 * sum(P) = target + sum(nums)
# 因此，原来的问题已转化为一个求子集的和问题： 找到nums的一个子集 P，使得上述等式成立

# 转换成0-1背包问题,和416题一样的思路,对于给定的nums,刚好装满j容量有dp[j]种方法, 只不过416题的target是0, 这个题的target是给定的S,学到了
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if sum(nums) < S or (sum(nums) + S) % 2 == 1: return 0
        P = (sum(nums) + S) // 2
        dp = [1] + [0 for _ in range(P)]
        for num in nums:
            for j in range(P, num - 1, -1):
                dp[j] = dp[j] + dp[j - num]
        return dp[P]


a = Solution().findTargetSumWays([50,30], 80)
print(a)
