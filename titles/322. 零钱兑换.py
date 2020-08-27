#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 简单的dfs., 不过即便先进行了倒序的排序最先拿到的组合数也仍然不是最小的,没想明白...
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:return 0
        coins.sort(reverse=True)
        def dfs(amount,cate):
            for i in coins:
                new_amount = amount - i
                if new_amount == 0:
                    return cate+1
                elif new_amount <0:
                    continue
                else:
                    res = dfs(new_amount,cate+1)
                    if res:
                        return res
        res=dfs(amount, 0)
        if res:
            return res
        else:return -1

import functools
# 思路倒是不新奇, 就是动态规划的状态转移, 但是学到了一些东西
# 1. 解决本地与网站不一致的方法,用成员变量self.coins = coins,而不是像之前那样一直用类变量
# 2. 初始化某个极大的最小值,该值没变化说明没找到目标,返回-1,找到了的话就不断更新, 使其最小
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @functools.lru_cache(amount)
        def dp(rem):
            if rem < 0: return -1
            if rem == 0: return 0
            mini = int(1e9)
            for coin in self.coins:
                res = dp(rem - coin)
                if res >= 0 and res < mini:
                    mini = res + 1
            return mini if mini < int(1e9) else -1

        self.coins = coins
        if amount < 1: return 0
        return dp(amount)


#这个方法看不太懂感觉很优雅的样子
# https://leetcode-cn.com/problems/coin-change/solution/322-ling-qian-dui-huan-by-leetcode-solution/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

a=Solution().coinChange([186,419,83,408],6249)
print(a)