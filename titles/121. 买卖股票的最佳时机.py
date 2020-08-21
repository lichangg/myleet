#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 双指针思路,左指针为买入价,右指针为卖出价
# 右指针向右移动找最高卖出价,动态更改最大收益
# 当遇到比左指针还低的价格时,左指针收缩过来,右指针继续向右找
# 执行用时：44 ms, 在所有 Python3 提交中击败了89.32%的用户
# 内存消耗：14.5 MB, 在所有 Python3 提交中击败了76.41%的用户
class Solution:
    def maxProfit(self, prices) -> int:
        l = 0
        max_profit = 0
        for i in range(1,len(prices)):
            if prices[i] < prices[l]:
                l = i
            else:
                max_profit = max(max_profit, prices[i] - prices[l])
        return max_profit
# 学到了
# 用动态规划 dp[i] 表示前 ii 天的最大利润，因为我们始终要使利润最大化，则：
# dp[i]=max(dp[i−1],prices[i]−minprice)

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         n = len(prices)
#         if n == 0: return 0 # 边界条件
#         dp = [0] * n
#         minprice = prices[0]
#
#         for i in range(1, n):
#             minprice = min(minprice, prices[i])
#             dp[i] = max(dp[i - 1], prices[i] - minprice)
#
#         return dp[-1]

a=Solution().maxProfit([7,1,5,3,6,4,0,6])
print(a)