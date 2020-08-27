#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 自己写的BFS,应该没啥问题,但是复杂度太高但是需要剪枝提高效率
class Solution:

    def maxCoins(self, nums: List[int]) -> int:
        root = (nums, 0)
        self.max_coins = 0

        def dfs(root):
            nums = root[0]
            for index, i in enumerate(nums):
                l = 1 if index - 1 < 0 else nums[index - 1]
                r = 1 if index + 1 > len(nums) - 1 else nums[index + 1]
                newcoins = root[1] + l * i * r
                self.max_coins = max(newcoins, self.max_coins)
                next_nums = nums[:]
                next_nums.pop(index)
                dfs((next_nums, newcoins))

        dfs(root)
        return self.max_coins

# 区间动态规划
# https://leetcode-cn.com/problems/burst-balloons/solution/zhe-ge-cai-pu-zi-ji-zai-jia-ye-neng-zuo-guan-jian-/
class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        #nums首尾添加1，方便处理边界情况
        nums.insert(0,1)
        nums.insert(len(nums),1)

        store = [[0]*(len(nums)) for i in range(len(nums))]

        def range_best(i,j):
            m = 0
            #k是(i,j)区间内最后一个被戳的气球
            for k in range(i+1,j): #k取值在(i,j)开区间中
                #以下都是开区间(i,k), (k,j)
                left = store[i][k]
                right = store[k][j]
                a = left + nums[i]*nums[k]*nums[j] + right
                if a > m:
                    m = a
            store[i][j] = m

        #对每一个区间长度进行循环
        for n in range(2,len(nums)): #区间长度 #长度从3开始，n从2开始
            #开区间长度会从3一直到len(nums)
            #因为这里取的是range，所以最后一个数字是len(nums)-1

            #对于每一个区间长度，循环区间开头的i
            for i in range(0,len(nums)-n): #i+n = len(nums)-1

                #计算这个区间的最多金币
                range_best(i,i+n)

        return store[0][len(nums)-1]

# 动态规划...以后看吧
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        points = [1] + nums + [1]
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for i in range(n, -1, -1):
            for j in range(i + 1, n + 2):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + points[i] * points[k] * points[j])
        return dp[0][-1]

test = [7,8,3,7,2,4,5]
b = Solution().maxCoins(test)
print(a)
print(b)
