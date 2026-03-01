#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 背包问题, 重点题
from functools import lru_cache
from typing import List

# 下面这个解法是有问题
# 思路是设置深度搜素dfs(amount,coins)方法表示组成amount的组合数, 问题在于
# 对于 3, [1,2]来说,根是3 ,第一层是[2, 1] 第二层是[1,0,0,-1],第三层是[0,-1,null,null,null,null,null,null]
# 想靠dfs(3) = dfs(2) + dfs(1)这个公式来解是不对的, 因为会重复, 对于2来说,确实是两种组合[1,1]和[2], 对于1来说也确实是1种组合[1]
# 对于3来说[1,1,1],[1,2],[2,1]  这其中后两者是重复的
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.count = 0
        self.cache = {}
        coins.sort()
        def dfs(amount, coins):
            if amount in self.cache:
                return self.cache[amount]
            if amount == 0:
                return 1
            if amount < 0:
                return 0
            count = 0
            for coin in coins:
                count += dfs(amount-coin, coins)
            self.cache[amount] = count
            return count
        res = 0
        for coin in coins:
            res += dfs(amount-coin, coins)
        return res
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if len(coins)==0:
            return 1 if amount==0 else 0
        coins.sort(reverse=True)
        @lru_cache(None)
        def dfs(amount,i):
            if len(coins[i:])==0:
                return 0
            if amount==0:
                return 1
            if amount<coins[-1]:
                return 0
            res = 0
            for idx,c in enumerate(coins[i:]):
                if c<=amount:
                    cnt = dfs(amount-c,i+idx)
                    res+=cnt
            return res
        return dfs(amount,0)


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        # 外层循环展示的是每增加一种硬币会对dp数组产生什么影响
        for coin in coins:
            # 内存循环的含义是
            # 1. 对某个硬币来说, 它影响不了比其值小的位置
            # 2. 对于比该硬币值大的位置来说, dp[x]表示的是在不用该硬币时凑成x一共的组合数, dp[x-coin]表示不用该硬币时凑成x-coin一共的组合数
            #    现在这枚硬币要用上了,所以更新dp[x] 为dp[x]+dp[x-coin]
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]


a=Solution().change(3,[1,2])
print(a)