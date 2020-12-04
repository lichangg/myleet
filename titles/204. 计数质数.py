#!/usr/bin/env python
# -*- coding:utf-8 -*-

from functools import lru_cache
from math import sqrt

# 如果不进行开方,也就是
# 会超时的,用了lrucache也没用的
class Solution:
    def countPrimes(self, n: int) -> int:
        res = []

        @lru_cache()
        def valid_zhishu(num):
            if num in {0, 1}:
                return False
            for i in range(2, int(sqrt(num))+1):

                if num % i == 0:
                    return False
            else:
                return True

        for j in range(1, n):
            if valid_zhishu(j):
                res.append(j)

        return len(res)

# 该算法用了 埃氏筛,核心逻辑就是
# 1. 若x是质数,那么2x,3x,4x...肯定不是质数
# 2. 若某数是合数h,那么在遍历到某个比它小的x的时候,一定会找到x*y=h,此时就会把h标记为合数了
# 3. 若某数是质数z,那么在一直遍历到z-1时都不可能找得到一个数使得z是该数的整数倍,而往后就更动不了这个z了

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:  # 题目：统计所有小于非负整数 n 的质数的数量，所以当n<=2时，无质数
            return 0
        isPrimes = [1] * n  # 构建一个值为1的数组，代表每一个数是合数
        isPrimes[0] = isPrimes[1] = 0  # 0和1不是质数，先置0排除
        for num in range(2, int(sqrt(n)) + 1):  # int（）range（）函数只能键入整数值
            if isPrimes[num]:  # 该值没有置0
                print([0] * ((n - 1 - num * num) // num + 1))
                isPrimes[num * num:n:num] = [0] * ((n - 1 - num * num) // num + 1)


        '''从num平方开始切片，因为之前的数已经处理了,例如7^7，如6*7,6就已经处理了'''
        return sum(isPrimes)

a = Solution().countPrimes(100)
print(sqrt(100))
