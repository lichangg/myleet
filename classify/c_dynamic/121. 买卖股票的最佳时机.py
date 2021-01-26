#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 用动态规划还不如野路子
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        dp = [[0]*2 for _ in range(l)]
        dp[0][0], dp[0][1] = -prices[0], 0
        i = 1
        max_profit = 0
        while i < l:
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            max_profit = max(dp[i][1], max_profit)
            i+=1
        return max_profit

a=Solution().maxProfit([7,1,5,3,6,4])
print(a)
