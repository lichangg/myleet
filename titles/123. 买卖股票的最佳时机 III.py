#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        dp = [[0]*5 for _ in range(l)]
        # 状态0表示第一次交易中有了股票, 1表示第一次交易已经完成, 2表示第二次交易中有了股票, 3表示第二次交易已经完成, 4表示不做任何操作(该状态可以去掉)
        dp[0][0], dp[0][1], dp[0][2], dp[0][3], dp[0][4] = -prices[0], 0, -prices[0], 0, 0
        i = 1
        max_profit = 0
        while i<l:
            dp[i][0] = max(- prices[i], dp[i-1][0])
            dp[i][1] = max(dp[i-1][0] + prices[i], dp[i-1][1])
            dp[i][2] = max(dp[i-1][1] - prices[i], dp[i-1][2])
            dp[i][3] = max(dp[i-1][2] + prices[i], dp[i-1][3], dp[i-1][4])
            max_profit = max(max_profit, dp[i][3])
            dp[i][4] = max(dp[i-1][4], dp[i-1][1])
            i+=1

        return max_profit

# 压缩了空间
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0
        for i in range(1, n):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2


a=Solution().maxProfit(prices = [1,2,3,4,5])
print(a)
