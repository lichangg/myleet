#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 自己写,裂开,主要是每个位置会有三种状态
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         days = len(prices)
#         dp = [0 for i in range(days)]
#         dp[0] = 0
#         dp[1] = max(prices[1]-prices[0], 0)
#         dp[2] = max(prices[1]-prices[0], prices[2]-prices[0],0)
#         print(dp)
#         for i in range(3, days):
#             last_profit = prices[i]-prices[i-1]
#             if last_profit>0:
#                 dp[i]= max(dp[i-1],dp[i-2] + last_profit)
#             else:
#                 dp[i] = dp[i-1]
#
#         return dp[-1]

# dp数组还可以不是一维的!!!学到了
# 每个dp位置右三种状态
# 1. 刚买入股票,
# 2. 不持股,刚卖出股票,下一个位置无法买入
# 1. 不持股,之前卖出了股票,处于自由期
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        # f[i][0]: 手上持有股票的最大收益
        # f[i][1]: 手上不持有股票，并且处于冷冻期中的累计最大收益
        # f[i][2]: 手上不持有股票，并且不在冷冻期中的累计最大收益
        f = [[-prices[0], 0, 0]] + [[0] * 3 for _ in range(n - 1)]

        for i in range(1, n):
            #此状态实际上记录了买入的最低价,非常精髓,学到了
            f[i][0] = max(f[i - 1][0], f[i - 1][2] - prices[i])

            f[i][1] = f[i - 1][0] + prices[i]

            f[i][2] = max(f[i - 1][1], f[i - 1][2])

        return max(f[n - 1][1], f[n - 1][2])

# 压缩空间, 优化了上一个算法
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices:
#             return 0
#
#         n = len(prices)
#         f0, f1, f2 = -prices[0], 0, 0
#         for i in range(1, n):
#             newf0 = max(f0, f2 - prices[i])
#             newf1 = f0 + prices[i]
#             newf2 = max(f1, f2)
#             f0, f1, f2 = newf0, newf1, newf2
#
#         return max(f1, f2)

b=[1,2,3,0,2]
a=Solution().maxProfit(b)
print(a)