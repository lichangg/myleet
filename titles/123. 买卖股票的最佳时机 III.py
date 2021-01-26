#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        dp = [[0]*4 for _ in range(l)]
        dp[0][0], dp[0][1], dp[0][2], dp[0][3] = -prices[0], -prices[0], 0, 0
        i = 1
        max_profit = 0
        while i<l:
            dp[i][0] = max(dp[i-1][2], dp[i-1][3]) - prices[i]
            dp[i][1] = max(dp[i-1][0], dp[i-1][1])
            dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + prices[i]
            dp[i][3] = max(dp[i-1][2], dp[i-1][3])
            max_profit = max(dp[i][2], dp[i][3], max_profit)
            i+=1
        while i<l:




a=Solution().maxProfit([3,3,5,0,0,3,1,4])
print(a)