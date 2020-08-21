#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List
from functools import lru_cache

# 这种递归会导致之前计算号的dp()用不上,得加上lru_cache才能不超时
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

# 非递归的动态规划写法,效率高,学到了
# 其实好像动态规划都是先初始化一个空的列表或是矩阵. 然后依次往里面填充数据
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]
        # 初始化好dp的长度
        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, size):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[size - 1]


a = Solution().rob([2,7,9,3,1])
print(a)
