#!/usr/bin/env python
# -*- coding:utf-8 -*-
# todo
from typing import List


# 1. 设置sell[i][j]为对于数组的0到i个价格(包括i), 交易j次, 且手上没有股票的状态
# 2. 设置buy[i][j]为对于数组的0到i个价格(包括i), 交易j次, 且手上有股票的状态
# 3. 状态转移buy[i][j] = max(sell[i - 1][j] - prices[i], buy[i - 1][j])
# 4. 状态转移sell[i][j] = max(sell[i - 1][j], buy[i - 1][j - 1] + prices[i])
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:return 0
        l = len(prices)

        sell = [[0] * (k+1) for _ in range(l)]
        # 一定要注意初始化的buy, 对于每一个交易0次的情况, 其手上持有股票的最大收益是到i为止最小的成本价格再取负
        buy = [[-min(prices[0:idx+1])] * (k+1) for idx in range(l)]

        i = 1
        while i < l:
            for j in range(1, k+1):
                buy[i][j] = max(sell[i - 1][j] - prices[i], buy[i - 1][j])
                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j - 1] + prices[i])
            i += 1
        return max(sell[-1])


a = Solution().maxProfit(k = 2, prices =[3,2,6])
print(a)
