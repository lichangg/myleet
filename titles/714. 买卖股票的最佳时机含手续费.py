#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp=[[0,0]]*len(prices)
        dp[0] = [-prices[0], 0]
        i = 1
        while i < len(prices):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i]-fee)
            i+=1
        return dp[-1][1]


a=Solution().maxProfit(prices = [9,], fee = 2)
print(a)