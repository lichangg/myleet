#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 学到了
# 动态规划数组有时候并不一定是要一次生成的,多次修改也是可以的!!!
# 复杂度为O(n2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]: # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                    # 此处一定要注意是由位置j来进行+1而不是由i的上一个位置进行+1
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

# 动态规划 + 二分查找, 复杂度为O(nlogn),暂时看不懂...
class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        tails, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tails[m] < num: i = m + 1 # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                else: j = m
            tails[i] = num
            if j == res: res += 1
        return res


a=Solution().lengthOfLIS()
print(a)