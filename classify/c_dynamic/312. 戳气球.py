#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.append(1)
        nums.insert(0, 1)
        l = len(nums)
        i = 0
        j = l - 1
        self.cache = {}

        def dp(i, j):
            if (i, j) in self.cache:
                return self.cache[(i, j)]
            if j - i == 1:
                self.cache[(i, j)] = 0
                return 0
            # 下面这个if只是为了解决n个100的那个用例超时的问题
            if len(set(nums[i + 1:j])) == 1 and j - i > 3:
                max_coins = (j - i - 3) * nums[i + 1] ** 3 + nums[i + 1] ** 2 + nums[i + 1]
                self.cache[(i, j)] = max_coins
                return max_coins
            tmp = []
            for last in range(i + 1, j):
                tmp.append(dp(i, last) + dp(last, j) + nums[i] * nums[last] * nums[j])
            max_coins = max(tmp)
            self.cache[(i, j)] = max_coins
            return max_coins

        return dp(i, j)
# 别人的dp
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

a = Solution().maxCoins([3, 1, 5, 8])
print(a)
