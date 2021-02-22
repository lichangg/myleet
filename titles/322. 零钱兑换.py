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


# 二刷, 先用贪心,贪心始终超时,难受
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort()
        # lru函数的奇怪之处啊
        # lru里面传的参数太小了会影响效率, 例如[357,239,73,52],9832 用这个测试用例,传个大数9999999就很快,传小的如55就很慢
        @functools.lru_cache(amount)
        def is_valid(count, amount):
            if amount == 0:
                return True
            if count == 0:
                return False
            for coin in coins:
                if is_valid(count-1, amount-coin):
                    return True

        for i in range(0 ,amount+1):
            if is_valid(i, amount):
                return i
        else:
            return -1

# 二刷, bfs会超时
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # coins.sort(reverse=True)
        level = None
        def bfs(amounts, level):
            new_amounts = []
            for amount in amounts:
                for coin in coins:
                    if amount == coin:
                        return level
                    new_amounts.append(amount - coin)
            return bfs(new_amounts, level+1)
        for coin in coins:
            if coin == amount:
                return 1
            level = bfs([amount], 1)
        return level or -1
# dfs思路不对, 因为尽管排序后深度搜索是往最大的路径搜的, 是最快到达负值的, 但是并不一定是最快恰好到达0的
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         coins.sort(reverse=True)
#         def dfs(amount,level):
#             if amount == 0:
#                 return level
#             if amount<0:
#                 return
#             for coin in coins:
#                 l = dfs(amount - coin, level+1)
#                 if l:
#                     return l
#         for coin in coins:
#             if coin == amount:
#                 return 1
#             l = dfs(amount, 0)
#             if l:
#                 return l
#         return -1

# 再刷,广度搜素先试试,
# 这样会导致很多达不到的remain重复计算,会超时
from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:return 0
        coins.sort(reverse=True)
        q = deque()
        q.append((amount, 0))
        while len(q) >= 1:
            remain,level = q.popleft()
            for i in coins:
                if remain > i:
                    q.append((remain-i, level+1))
                elif remain == i:
                    return level +1
        return -1

# dp[i]表示组成i需要的最少的数字个数
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [-1] * (amount+1)
        dp[0] = 0
        for index in range(0,amount+1):
            if dp[index] == -1:
                continue
            for coin in coins:
                if index+coin>amount:
                    break
                if dp[index+coin]>=1:
                    dp[index+coin] = min(dp[index+coin], dp[index]+1)
                else:
                    dp[index+coin] = dp[index] + 1

        return dp[amount]


a=Solution().coinChange(
[357,239,73,52],
9832)
print(a)