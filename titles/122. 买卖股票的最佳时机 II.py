#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 思路: 动态规划
# 每天结束后有两种持有状态,每个持有状态又各自分两种情况,所以一共四种情况.分别是:
#   - 手上有股票, 且是今天买的
#   - 手上有股票, 且是以前买的
#   - 没有股票, 且是今天卖的
#   - 没有股票, 且是以前就卖掉了
# 每一种都对应一个状态转移方程,
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        dp = [[0]*4 for _ in range(l)]
        # 需要注意初始时候,若结束时既然要算有的情况, 因为没法在以前买, 所以只能今天买, 所以两个状态都是 -prices[0]
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
        return max_profit
# 其实可以不用上述4中状态, 只需要持有股票和不持有股票两种状态就行了
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        dp = [[0]*2 for _ in range(l)]
        dp[0][0], dp[0][1] = 0, -prices[0]
        max_profit = 0
        i = 1
        while i<l:
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])
            max_profit = max(dp[i][0], max_profit)
            i+=1
        return max_profit
a=Solution().maxProfit([1,2,3,4,5])
print(a)