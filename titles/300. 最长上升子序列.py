#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


# 学到了
# 动态规划数组有时候并不一定是要一次生成的,多次修改也是可以的!!!
# 复杂度为O(n2)
# 动态规划数组中的索引dp[i]的意义为, 以nums[i]为终点的最长上升序列的长度
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                    # 此处一定要注意是由位置j来进行+1而不是由i的上一个位置进行+1
                    # 此处会选择取dp[j]+1还是已经累加好的dp[i], 取dp[j]+1的意义就是在承认j为上一个上升子序列的终点, +1就得到了以当前i为终点的值(且经过j)
                    # 因为dp[i]在不断累加, 所以其实有可能dp[i]已经累加超过了dp[j],这个时候就不能经过j
                    # 例如[1,3,6,7,4,10],在算10的位置的时候就不能经过4
                    dp[i] = max(dp[j] + 1, dp[i])
                    # dp[i] = dp[j] + 1
        return max(dp)


# 动态规划 + 二分查找, 复杂度为O(nlogn),暂时看不懂...,
# 二刷时仍然看不懂
class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        tails, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tails[m] < num:
                    i = m + 1  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                else:
                    j = m
            tails[i] = num
            if j == res:
                res += 1
        return res


# 二刷失败

a = Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 21, 18])
print(a)
