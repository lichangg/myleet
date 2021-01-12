#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

#  思路1. 层序遍历, 如果遇到amount太大的话, 要往下找很久才,会超时
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         self.coins = coins
#         if amount == 0:
#             return 0
#         def dfs(cur_amounts, level):
#
#             curs = []
#             for cur in cur_amounts:
#                 if cur < 0:
#                     continue
#                 for c in self.coins:
#                     if cur- c == 0:
#                         return level
#
#                     else:
#                         curs.append(cur-c)
#             if not curs:
#                 return
#             res = dfs(curs, level+1)
#             if res:
#                 return res
#
#         level = 1
#         curs = []
#         for i in self.coins:
#             cur = amount - i
#             if cur == 0:
#                 return level
#             elif cur < 0:
#                 continue
#             else:
#                 curs.append(cur)
#         res = dfs(curs, level+1)
#         return res or -1


from functools import lru_cache
import heapq
# 思路2 还是得用动态规划, 定义dp[i]为构建amount=i的金额所需要的最少硬币数
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0
        coins.sort(reverse=True)
        self.coins = coins
        @lru_cache(amount)
        def dp(amount):
            if amount <0:
                return
            mini = float('inf')
            for i in self.coins:
                if amount - i == 0:
                    return 1
                pre_dp = dp(amount-i)
                if not pre_dp:
                    continue
                # tmp.append(pre_dp)
                mini = min(mini, pre_dp)

            if mini == float('inf'):
                return
            return mini + 1
        return dp(amount) or -1

# 思路3 还是动态规划, 只不过这次是填动态规划的数组,定义dp[i]为构建amount=i的金额所需要的最少硬币数
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
a=Solution().coinChange([8,7,5,1],
19)
print(a)