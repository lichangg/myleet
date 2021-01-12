#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

# 思路1.暴力法(带了一点点动态规划)
# 两次循环,外循环固定一个数,含义为以该数为子序列的起始数, 以该数的下一个数做内循环起点, 累计算出序列和并看看能不能整除k
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        l = len(nums)
        if l<=1:
            return False
        if k == 0:
            c = 0
            while c<l:
                if nums[c] == 0 and (c+1<l and nums[c+1] == 0):
                    return True
                c+=1
            return False
        # cache = {}
        for i in range(0, l):
            sum_i = nums[i]
            for j in range(i+1, l):
                sum_i += nums[j]
                # cache[sum_i] = True
                if divmod(sum_i, k)[1] == 0:
                    return True
        return False
a=Solution().checkSubarraySum([1,0], k = 2)
print(a)