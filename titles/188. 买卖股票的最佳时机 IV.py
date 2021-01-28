#!/usr/bin/env python
# -*- coding:utf-8 -*-
# todo
from typing import List


# 设置sell[i][j]为对于数组前i个价格, 交易j次, 且手上没有股票的状态
# 设置buy[i][j]为对于数组前i个价格, 交易j次, 且手上有股票的状态
# 状态转移buy[i][j] = max(sell[i-1][j], buy[i-1][j] - prices[i])
# 状态转移sell[i][j] = max(sell[i-1][j], buy[i-1][j] - prices[i])
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        l = len(prices)
        sell = [[0] * k for _ in range(l)]
        buy = [[0] * k for _ in range(l)]
        sell[0][0] = 0
        buy[0][0] = -prices[0]
        i = 1
        while i < l:
            for j in range(k):
                buy[i][j] = max(sell[i - 1][j] - prices[i], buy[i - 1][j])
                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j - 1] + prices[i])
            i += 1
        return max(sell[-1])


a = Solution().maxProfit(k=2, prices=[3, 2, 6, 5, 0, 3])
print(a)
